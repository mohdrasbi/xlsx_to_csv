from flask import Flask, render_template, request
import pandas as pd
from io import BytesIO


app = Flask(__name__)
app.secret_key = "testtt123444"


@app.route('/', methods=['POST', 'GET'])
def index():
	upload_file_msg = ""
	success = False

	if request.method == "POST":
		if "file" not in request.files:
			upload_file_msg = "Please select a file."
			success = False

		else:
			file = request.files['file']

			if file.filename == "":
				upload_file_msg = "Please select a file."
				success = False
			elif "xlsx" not in file.filename:
				upload_file_msg = "Please select an xlsx file."
				success = False
			elif file:
				excel_df = pd.read_excel(BytesIO(file.read()))
				csv_filename = '{}.csv'.format(file.filename.split('.')[0])
				excel_df.to_csv(csv_filename, encoding='utf-8', index=False)

				upload_file_msg = "Converted file successfully. Saved as {} in your current directory.".format(csv_filename)
				success = True



	return render_template('index.html', upload_file_msg=upload_file_msg, success=success)



if __name__ == "__main__":
	app.run()