from pyscript import display, document

# This function runs when the "Sign up!" button is clicked
def intrams_checker(e):
    # Clear previous output messages and images
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '

    # Get the selected registration radio button (Yes/No)
    registration_el = document.querySelector(
        'input[name="registration"]:checked'
    )
    # Get the selected medical clearance radio button (Yes/No)
    clearance_el = document.querySelector(
        'input[name="clearance"]:checked'
    )

    # If the user did not select registration or clearance, show an error
    if not registration_el or not clearance_el:
        display(
            "❌ Please answer all the questions before proceeding.",
            target="output"
        )
        return  # Stop the function here if any question is unanswered

    # Get the values of the selected options
    registration = registration_el.value  # "registered" or "not_registered"
    clearance = clearance_el.value        # "cleared" or "not_cleared"

    # Get the grade level from the dropdown (convert to number)
    grade_level = int(document.getElementById('level').value)
    # Get the section from the dropdown (emerald, ruby, sapphire, topaz)
    section = document.getElementById('section').value

    # Check if the user is eligible for Intramurals
    if registration != 'registered':
        # User is not registered yet
        display(
            "😞 Not eligible. You are not yet registered for Intramurals.",
            target='output'
        )
    elif clearance != 'cleared':
        # User does not have medical clearance
        display(
            "😞 Not eligible. Medical clearance is required.",
            target='output'
        )
    # If user passed registration and clearance, assign team based on section
    elif section == 'emerald':
        display(
            "🎉 Congratulations!!! 💚\n"
            "Welcome to Green hornets — strength, unity, and sportsmanship!",
            target='output'
        )
        # Show corresponding image for the team
        document.getElementById("image").innerHTML = "<img src='Green.png' width='300'>"
    elif section == 'ruby':
        display(
            "🎉 Congratulations!!! ❤️\n"
            "You are officially part of Red bulldogs — passion and power on the field!",
            target='output'
        )
        document.getElementById("image").innerHTML = "<img src='Red.png' width='300'>"
    elif section == 'sapphire':
        display(
            "🎉 Congratulations!!! 💙\n"
            "Blue bears it is — calm minds, sharp skills, strong wins!",
            target='output'
        )
        document.getElementById("image").innerHTML = "<img src='Blue.png' width='300'>"
    else:
        # If section is "topaz" or anything else, assign Yellow tigers
        display(
            "🎉 Congratulations!!! 💛\n"
            "Welcome to Yellow tigers — bright energy and unstoppable teamwork!",
            target='output'
        )
        document.getElementById("image").innerHTML = "<img src='Yellow.png' width='300'>"




