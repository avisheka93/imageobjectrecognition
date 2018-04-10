import os
from app import flaskapp
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	flaskapp.run(host='0.0.0.0', port=int(port),debug=True)
	print("app started on port",port);