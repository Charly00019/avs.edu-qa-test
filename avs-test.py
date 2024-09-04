# This script contains python packages that must be installed 
# Make sure you install requirement.txt
# Also make sure to purchase a new voucher and change to own in the script
# Check line 25 and 27

import os
import pyautogui
import time
from seleniumbase import BaseCase


class MyTestClass(BaseCase):
    def test_basic(self):
        # Open a website
        self.open("https://qa.avs.edu.gh/")

        # Assert that the title contains "Example"
        self.assert_title_contains("Aurora Verus School")

        
        # Hover over the menu item to reveal the dropdown
        self.hover_and_click("#admissions", "#navbarCollapse > div > div > div > a:nth-child(2)")
        self.assert_text("Let's get started!", "h1")
        self.click("#voucher_serial_number")
        self.send_keys("#voucher_serial_number", "RFMFNR199A")
        self.click("#voucher_pin")
        self.send_keys("#voucher_pin", "465905824")
        self.click("body > div.container-fluid.pt-5.all-forms > div > div.col-lg-5 > div > div > form > div:nth-child(6) > input")

        # Assert text on the page to determine the current state
        if self.is_text_visible("Welcome"):
            # If the text for Page Version 1 is visible
            self.assert_text("Welcome", "body > div.container-fluid.pt-5.all-forms > div:nth-child(1) > div > div > div.text-center > h3")
            # Continue with actions specific to Page Version 1
            # self.scroll_to("a.remove-undline.stretched-link")

            # self.wait_for_element_visible("a.remove-undline.stretched-link", timeout=15)

            # self.hover_and_click('a.remove-undline.stretched-link', 'a.remove-undline.stretched-link')

            self.click("body > div.container-fluid.pt-5.all-forms > div:nth-child(2) > div:nth-child(1) > div > div")
        elif self.is_text_visible("Profile Picture"):
            # If the text for Page Version 2 is visible
            self.assert_text("Profile Picture", "#tab1 > div > h4")
            # Continue with actions specific to Page Version 2
        else:
            # Handle the case where neither text is found
            self.fail("Neither expected text was found on the page.")

        # Continue with your test
        # get the new url and assert if true
        expected_prefix = "https://qa.avs.edu.gh/apply/"

        admission_portal_url=self.get_current_url()
        self.assert_true(admission_portal_url.startswith(expected_prefix), f"URL does not start with {expected_prefix}")

         # Assert that an form element is visible
        self.assert_text("Application Form","h2")

        # select image for profile
        self.click("#selectImageButton")

        # define file path
        file_path = os.path.join(os.getcwd(),"for-avs-test.jpeg")

        #chooosing the file
        self.choose_file("#file-input", file_path)

        pyautogui.press('esc')

        # upload image
        self.click("#saveImageButton")

        self.scroll_to("h4")

        
        self.assert_text("Basic Details","#tab2 > div > h4")  # Waits up to 15 seconds
        self.click("#id_first_name")
        self.send_keys("#id_first_name", "Aurora")
        self.click("#id_last_name")
        self.send_keys("#id_last_name", "Verus")
        self.click("#id_date_of_birth", timeout=10)
        
        # Select the date 15th March 2009
        self.set_value("#id_date_of_birth", "2009-03-21")

        self.click("#id_gender")
        self.select_option_by_text("#id_gender", "Female")
        self.click("#id_religion")
        self.select_option_by_text("#id_religion", "Other")
        self.click("#saveBioDataButton")
        
        # Assert if the identification details has load and fill in the details
        self.assert_text("Identification Details", "#tab3 > div > h4")

        self.select_option_by_text("#id_nationality", "Burkinabe")
        self.select_option_by_text("#id_national_id_type", "Passport")
        self.send_keys("#id_national_id_no", "012345679")
        self.click("#id_national_id_issue_date")
        self.set_value("#id_national_id_issue_date", "2019-03-21")
        self.click("#id_national_id_expiry_date")
        self.set_value("#id_national_id_expiry_date", "2026-03-21")

         # define file path
        self.click("#id_national_id_pic")

        file_path_1 = os.path.join(os.getcwd(),"for-id.tif")

        #chooosing the file
        self.choose_file("#id_national_id_pic", file_path_1)
        pyautogui.press('esc')
        self.click("#saveIdentificationButton", timeout=15)

         # Assert if the guardian information has load and fill in the details
        self.assert_text("Guardian Information", "#tab4 > div > h4", timeout=15)
        self.send_keys("#id_guardian_name", "Able God")
        self.send_keys("#id_residence", "Ak1234")
        self.send_keys("#id_primary_phone", "0244919191")
        self.send_keys("#id_secondary_phone", "0505714200")
        self.send_keys("#id_guardian_email", "Ak1234")
        self.click("#saveGuardianButton")

        # Assert if Prefered Class portal is available and fill in
        self.assert_text("Prefered Class", "#tab5 > div > h4")
        self.click("#id_proposed_class")
        self.select_option_by_text("#id_proposed_class", "KG 1")
        self.click("#saveClassButton")

        # Assert if Prefered Education History is available and fill in
        self.assert_text("Education History", "#tab6 > div > h4")
        self.send_keys("#id_institution", "Havard kiddie care")
        self.set_value("#id_start_date", "2023-03-21")
        self.set_value("#id_end_date", "2024-03-21")
        self.send_keys("#id_location", "Havard City")
        self.select_option_by_text("#id_region", "Oti")
        self.select_option_by_text("#id_reason_for_leaving", "American")

        # save education history and submit the form

        self.click("#saveEducationButton")
        self.click("#skipEducationButton")
        self.assert_element_present("#prevSubmitButton")
        self.click("#prevSubmitButton")

        # confirm submission
        self.assert_text("Are you sure?", "#swal2-title")
        self.click("body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-confirm.swal2-styled.swal2-default-outline")

       
    if __name__ == "__main__":
        run(MyTestClass)
        



