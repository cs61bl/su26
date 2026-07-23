---
layout: page
title: "Checkoffs"
nav_order: 5
parent: >-
    Project 3
# grand_parent: Projects
has_children: false
has_toc: false
has_right_toc: true
description: >-
  Project 3 Checkoffs.
released: true
---

## Deadlines

{% capture deadlines %}{% include proj3-deadlines.html %}{% endcapture %}
{{ deadlines | markdownify }}


## Policies

Project 3 demos will be conducted during office hours from Wednesday to Friday (4/29-5/1).

{: .TASK}
> Upon 5C release sign up for a check off slot and complete it at your assigned time. 
> * See the Ed announcement for more details.
> * Make sure to prepare accordingly to avoid any last-minute emergencies!

The code that you present during your demo should be the code that you submitted to the Project 5C assignment on Gradescope. In other words, the Project 5C due date (plus any extensions you requested) is the deadline for making any changes to your code. Even if your checkoff doesn't happen until later, you can't make any changes after your Project 5C due date.

{: .WARNING}
The following is what the Autograder and TA will exactly do when checking you off: we recommend you do a dry-run of this to ensure you didn't miss anything. You can clone your repository in some random destination on your computer (like your home directory) if you want to follow along and simulate your checkoff.

## Attendance

Both partners should be present **in person** for the checkoff.

{: .NOTE}
> Please fill out the [Checkoffs Extenuating Circumstances Form](https://docs.google.com/forms/d/e/1FAIpQLSeZGDPqYpPanPtZNALyBFW7e5dpxCGYPpCVhTdp9TEyORnTMw/viewform?usp=dialog) if you are experiencing [extenuating circumstances](https://{{ site.semester_slug }}.datastructur.es/policies/extensions/#extenuating-circumstances) and need accommodations for the following:
> * Need to be checked off outside of the usual week of checkoffs (4/27–5/1), AND/OR
> * Need to be checked off online
> 
> **The deadline for this form is Tuesday, April 28th at 11:59PM (Project 5C deadline).** We cannot guarantee any accommodations if you do not submit this form by then.

## Setup

Designate one partner to be the presenter; this should be the partner who signed up for the demo slot. They should make sure to already have the following set up:
- IntelliJ open with your Project 5 code (doesn't matter what class)
- The program running with the BYOW main menu displayed
- The state of your repo should be the commit containing the version of your project you want to demo. The code you demo should be the same as the code you submitted to Gradescope. If this is your most recent commit, just make sure your Git status is clean. If it is a past commit, you can get to this state by running `git switch --detach <commit id>`. (To get your repo back to normal, run `git switch main`.)
- If you choose to demo a version of your project that is past the deadline (for a percentage penalty, per the syllabus), make sure to let the TA know.
- Your Git status should be clean (no changes to commit)

## Checkoff Script

Note that most interactivity features have been moved to an autograder. Only the Pathfinder task, and ambition features will be done live with a TA.

1. The grader will ask for your SID to find your group and then confirm names, SIDs, and group number.
2. One partner should designate their laptop as the "check-in laptop", and already have a terminal window in their `{{ site.semester_slug }}-proj5-g***/proj5`. Their Git should be in a clean state (git status should be clean), IntelliJ should be open, and the Project 5 main menu should be running.
   - If any of these requirements are not fulfilled, you may not receive a grade for Proj5 checkoff.
3. Run "git log" and make sure that the HEAD commit is a commit from before the deadline. Run "pwd". Make sure the path
   matches that of the open IntelliJ window.
4. The grader will then ask you to demonstrate the Pathfinder Task.
5. The grader will then ask you to demonstrate your ambition features, along with saving and loading (must save state of ambition feature).
6. The grader will tell you which items you received/did not receive credit for. They will ask if you agree with your score: if you do not, you will have the opportunity to request a regrade within 24 hours of your checkoff. This can be done under the Checkoff tab in Beacon.

### Basic World Functionality (100 points total) - Autograder

The Autograder will run your project and will check for the following features:

- The world has a main menu screen with a New World, Load, and Quit option
- The Autograder will hit "n" or "N" (they may do either) and check that the world prompts for a seed
- The Autograder will type in a few random numbers and hit "s" or "S" (they may do either) which should immediately start the world.

At this point, the program should be running and there should be a visible world.

- World has visually distinct walls and floors
- World has at least two hallways which are 1 tile wide
- World has at least 1 hallway containing a turn in it. If current world doesn't, ask students to generate a world that has a turning hallway.
- World has some number of rooms that are connected via hallways

The Autograder will now try the basic commands that should be available during gameplay.

- Autograder should hit the W, A, S, and D keys randomly and check the player movement is consistent with the key pressed
- Autograder should hover over 3 different tiles and make sure their names show up somewhere on screen and that the names make sense
- Autograder should verify that the HUD does not flicker
- Autograder should move into a wall and make sure the player stops at the wall instead of moving into it
- Autograder should type ":q" or ":Q" (they may do either) in "world mode" which should quit the world and close the program. Autograder should remember the world layout at this point

The program is now closed, and we will test the load feature.

The Autograder will run the world again after it has been closed and the main menu should appear again.

- Autograder will hit "l" or "L" and the world should immediately start
- Autograder will check that the world layout is exactly as it was before closing the world
- Autograder will run through the basic commands again (listed above) to make sure the world still works
- Autograder will quit and load again and make sure that the basic commands work
- Autograder will check that "q" or "Q" alone in "world mode" does not quit the game

### Randomness (50 points total)

- The Autograder will close the world again and will begin testing to see if worlds are randomly generated.
- Autograder will check that the use of randomness does not lead to a severe limitation on the variety of worlds (ie. randomly choosing a world layout from a finite set of worlds)
- The Autograder will open the world 3-5 times, making sure to use a different seed each time
- The Autograder will be looking for your world's ability to generate variety in both world structure and player experience while exploring that world. What this means is when two different seeds are used to generatge new worlds, these worlds should not feel identical (or close to identical).

### Pathfinder (60 points total)
- The TA will click a square, and path will be drawn to that square. This must be a shortest path.
- The TA will click the same square, and the avatar will be animated and moved to that square following the path

### Ambition Points (110 points total)

- The student should state and demonstrate the features that are in the Ambition category. You should be very explicit about how to "activate" or use that feature.
- The TA will write in the features the student successfully demonstrated and their point values based on the spec.
