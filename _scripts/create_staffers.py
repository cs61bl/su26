from csv import DictReader
import re
from yaml import load, dump
from google_drive_downloader import GoogleDriveDownloader as gdd
import os.path
from PIL import Image

"""
The purpose of this script is to generate the 2 .yml files for tas + tutors
to display on the course website. Steps:

1. Install the packages in requirements.txt

2. Convert staff responses into a separate spreadsheet with just the following
   information (must be done before invoking this script):

        a. Email Address
        b. Full Name
        c. Bio
        d. Appointment ('ta' or 'tutor' or 'ti')
        e. Photo (a link to a photo on google drive, make sure sharing is set to 'Anyone with link')
        f. Pronouns
        g. Personal Website (optional link to personal website)
        h. Staff Email Access (yes/no)
        i. DSP Data Access (yes/no)
        j. Student Support Data Access (yes/no)

3. Download .csv and place in this directory.

4. Invoke this script which will ask for the .csv filename, which then downloads
   all the images to the assets directory and updates the .yml files

NOTE: If we keep repeatedly trying, Google Drive will pick up and temporarily
network ban you from accessing the photos, so be aware of that.
NOTE: If an image is not showing up, verify that underlying filetype is correct (people who use .HEIC will likely have a broken image). If the issue persists, rerun the script.

@author: onk
@author: 22anirudhk

"""

IMG_ID_PATTERN = r'((?:\w|-){33})'

long_line = '-' * 50

csv_file_name = "staff.csv"

email = "Email Address"
name = "Full Name"
bio = "Bio"
appointment = "Appointment"
photo_link = "Photo"
pronouns = "Pronouns"
website_link = "Personal Website"
staff_email_access = "Staff Email Access"
dsp_data_access = "DSP Data Access"
student_support_data_access = "Student Support Data Access"

# Columns the script requires to function. Access columns are optional and
# default to "no access" when absent.
required_columns = [email, name, bio, appointment, photo_link, pronouns, website_link]
optional_columns = [staff_email_access, dsp_data_access, student_support_data_access]

def process_image(image_path, size=(256, 256)):
    """Crops, resizes, and compresses an image to be a square WebP."""
    try:
        with Image.open(image_path) as img:
            # Convert to RGB if necessary (for PNGs with alpha channel)
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Crop to square
            width, height = img.size
            if width != height:
                new_dim = min(width, height)
                left = (width - new_dim) // 2
                top = (height - new_dim) // 2
                right = left + new_dim
                bottom = top + new_dim
                img = img.crop((left, top, right, bottom))

            # Resize to target size
            if img.size[0] > size[0]:
                img.thumbnail(size, Image.Resampling.LANCZOS)

            # Save with compression
            img.save(image_path, 'webp', quality=95, method=6)
    except Exception as e:
        print(f"Error processing image {image_path}: {str(e)}")


with open(csv_file_name, newline='') as csvfile:
    reader = DictReader(csvfile)
    # Validate that all required columns exist (match header names directly)
    missing_columns = [col for col in required_columns if col not in reader.fieldnames]
    if missing_columns:
        print("Error: The following required columns are missing from the CSV:")
        for col in missing_columns:
            print(f"- {col}")
        exit(1)

    # Check for extraneous columns (optional access columns are not extraneous)
    known_columns = required_columns + optional_columns
    extra_columns = [col for col in reader.fieldnames if col not in known_columns]
    if extra_columns:
        print("\nWarning: The following columns are not required and will be ignored:")
        for col in extra_columns:
            print(f"- {col}")
        print("\nYou may want to remove these columns from your CSV file to keep it clean.")
        print(long_line)

    for row in reader:
        md = '---\n'
        staff_member = {}
        staff_member['email'] = row[email]
        staff_member['name'] = row[name]
        staff_member['bio'] = row[bio]

        # Flexible appointment handling
        raw_appointment = row[appointment].lower()
        if 'head' in raw_appointment:
            staff_type = 'Head TA'
        elif 'ta' in raw_appointment:
            staff_type = 'TA'
        elif 'tutor' in raw_appointment:
            staff_type = 'Tutor'
        elif 'ti' in raw_appointment:
            staff_type = 'TI'
        elif 'instructor' in raw_appointment:
            staff_type = 'Instructor'
        else:
            print(f"Warning: Unknown appointment type '{raw_appointment}' for {row[name]}")
            staff_type = 'unknown'

        gdrive_link = row[photo_link]
        _name = staff_member['name']

        staff_member['photo'] = None
        staff_member['pronouns'] = row[pronouns]

        # Add https:// if a website was provided and lacks a scheme
        raw_website = row[website_link] or ''
        if raw_website and not raw_website.startswith('http'):
            staff_member['link'] = 'https://' + raw_website
        else:
            staff_member['link'] = raw_website

        # Use underscore-separated lowercase name for image filename
        underscored_name = _name.lower().replace(' ', '_')
        img_path = f'{underscored_name}.webp'
        full_img_path = os.path.join(os.getcwd(), os.pardir, 'assets/', 'staff/', img_path)

        staff_member['photo'] = img_path

        md += 'name: ' + _name + '\n'
        md += 'pronouns: ' + staff_member['pronouns'] + '\n'
        md += 'role: ' + staff_type + '\n'

        # Add relevant access tags (default to no access if column absent)
        if row.get(staff_email_access, '').lower() == "yes":
            md += 'spaaccess: true\n'
        if row.get(dsp_data_access, '').lower() == "yes":
            md += 'dspdata: true\n'
        if row.get(student_support_data_access, '').lower() == "yes":
            md += 'studentSupportData: true\n'

        md += 'email: ' + staff_member['email'] + '\n'
        md += 'photo: ' + img_path + '\n'
        md += 'website: ' + str(staff_member['link']) + '\n'

        if os.path.exists(full_img_path):
            print(f'Skipping existing image for {_name}')
        else:
            if re.findall(IMG_ID_PATTERN, gdrive_link) == []:
                print(f'Bad link for {_name}, not downloading image: {gdrive_link}')
            else:
                img_id = re.findall(IMG_ID_PATTERN, gdrive_link)[0]
                try:
                    gdd.download_file_from_google_drive(
                        file_id=img_id,
                        dest_path=full_img_path,
                        overwrite=True,
                    )

                    # Process the downloaded image
                    process_image(full_img_path)

                    print(gdrive_link)
                except:
                    print(f"Gdrive photo could not be accessed for {row[name]}")

        md += '---' + '\n\n'
        md += staff_member['bio']
        file_name = underscored_name + '.md'
        file_path = os.path.join(os.getcwd(), os.pardir, '_staffers/', file_name)
        with open(file_path, 'w') as file:
            file.write(md)