from pyscript import display, document

def intrams_checker(e):
    # Clear previous output messages and images
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '

    # Get the selected registration and clearance radio buttons
    registration_el = document.querySelector('input[name="registration"]:checked')
    clearance_el = document.querySelector('input[name="clearance"]:checked')

    # Get the grade level and section dropdown elements
    grade_el = document.getElementById('level')
    section_el = document.getElementById('section')

    # Check that all required fields are filled
    required_fields = [registration_el, clearance_el, grade_el.value, section_el.value]
    if any(field is None or field == '' for field in required_fields):
        display("❌ Please answer all the questions before proceeding.", target="output")
        return

    # Get values
    registration = registration_el.value        # "registered" or "not_registered"
    clearance = clearance_el.value              # "cleared" or "not_cleared"
    grade_level = int(grade_el.value)
    section = section_el.value

    # Do nothing if both radio buttons have the same value (both Yes or both No)
    if registration == clearance:
        return

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
        document.getElementById("image").innerHTML = (
            "<img src='Green.png' width='300'>"
        )

    elif section == 'ruby':
        display(
            "🎉 Congratulations!!! ❤️\n"
            "You are officially part of Red bulldogs — passion and power on the field!", 
            target='output'
        )
        document.getElementById("image").innerHTML = (
            "<img src='Red.png' width='300'>"
        )

    elif section == 'sapphire':
        display(
            "🎉 Congratulations!!! 💙\n"
            "Blue bears it is — calm minds, sharp skills, strong wins!", 
            target='output'
        )
        document.getElementById("image").innerHTML = (
            "<img src='Blue.png' width='300'>"
        )

    else:
        # If section is "topaz" or anything else, assign Yellow tigers
        display(
            "🎉 Congratulations!!! 💛\n"
            "Welcome to Yellow tigers — bright energy and unstoppable teamwork!", 
            target='output'
        )
        document.getElementById("image").innerHTML = (
            "<img src='Yellow.png' width='300'>"
        )






