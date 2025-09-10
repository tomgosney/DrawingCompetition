**Drawing Competition **

Simple Python GUI application built with Tkinter for users to draw artwork and save it, along with their personal details to local files. Created to further my knowledge on creating Python GUI with Tkinter and saving files with python.

**Features**

	•	Interactive drawing canvas where users draw using their mouse.
	•	Data entry form for first name, last name, date of birth, gender and occupation.
	•	Permission checkbox for data collection consent.
	•	Save drawing as a high-quality PNG file (converted from PostScript).
	•	Store user details in a CSV file (Submissions.csv).
	•	Option to clear the canvas after submission or if user is unhappy with their artwork.

**How It Works**

	1.	Run the program with Python
	2.	Enter your details in the form.
	3.	Draw on the canvas using your mouse.
	4.	Submit your drawing and details.
	5.	The drawing is saved as a PNG image, and the details are logged in a CSV file.

**Requirements**

	•	Python 3.x
	•	Tkinter (comes with Python standard library)
	•	Ghostscript (for converting .ps to .png)

**File Outputs**

	•	Drawings: Saved in .png format in the project folder.
	•	Submissions.csv: Stores user details with submission metadata.
 
**Example CSV Row**

First Name, Last Name, Gender, Occupation, Date of Birth, Submission Name
John, Doe, Male, Student, 01-01-2000, JohnDoe:2025-09-10_22:30

**Future Improvements**

	•	Add more drawing tools (colors, brush sizes).
	•	Allow saving multiple drawings per user.
	•	Improve layout and styling.
