from flask import Flask, render_template, request, Response
import pandas as pd
from io import StringIO, BytesIO


app = Flask(__name__)
app.secret_key = "testtt123444"


@app.route('/', methods=['POST', 'GET'])
def index():
	upload_file_msg = ""

	if request.method == "POST":
		if "file" not in request.files:
			upload_file_msg = "Please select a file."
			success = False

		else:
			file = request.files['file']

			if file.filename == "":
				upload_file_msg = "Please select a file."
			elif "xlsx" not in file.filename:
				upload_file_msg = "Please select an xlsx file."
			elif file:
				excel_df = pd.read_excel(BytesIO(file.read()))
				csv_filename = '{}.csv'.format(file.filename.split('.')[0])

				return Response(
			        StringIO(excel_df.to_csv(index=False)),
			        mimetype='text/plain',
			        headers={"Content-Disposition": "attachment;filename={}".format(csv_filename)}
			    )



	return render_template('index.html', upload_file_msg=upload_file_msg)



if __name__ == "__main__":
	app.run(host='0.0.0.0')