from main import app
import os
app.config['UPLOAD_FOLDER'] = 'controller/uploads'

def test_home_route():
    # create a test client
    with app.test_client() as client:
        # make a request to the home page
        response = client.get('/')

        # check that the response status code is 200 OK
        assert response.status_code == 200

        # check that the response data contains the expected text
        # assert b'Welcome to my Flask app!' in response.data


def test_success_route():
    # create a test client
    with app.test_client() as client:
        # create a temporary file to upload
        with open('test_file.xlsx', 'w') as f:
            f.write('This is a test file.')

        # make a POST request to the upload route with the file attachment
        with open('test_file.xlsx', 'rb') as f:
            client.post('/success', data={'file': (f, 'test_file.xlsx')})

        # check that the file was uploaded successfully
        uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'test_file.xlsx')
        assert os.path.isfile(uploaded_file_path)
        
        # delete the temporary file
        os.remove('test_file.xlsx')


def test_progress_route():
    # create a test client
    with app.test_client() as client:
        # create a temporary file to upload
        with open('test_file2.xlsx', 'w') as f:
            f.write('This is the second test file.')

        # make a POST request to the upload route with the file attachment
        with open('test_file2.xlsx', 'rb') as f:
            client.post('/progress', data={'file': (f, 'test_file2.xlsx')})

        # check that the file was uploaded successfully
        uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'test_file2.xlsx')
        assert os.path.isfile(uploaded_file_path)
        
        # delete the temporary file
        os.remove('test_file2.xlsx')


def test_download_route():
    # create a test client
    with app.test_client() as client:
        # make a request to the about page
        response = client.get('/download')

        # check that the response status code is 200 OK
        assert response.status_code == 200

        # check that the response data contains the expected text
        # assert b'This is the about page.' in response.data

def test_download_files():
    # create a test client
    with app.test_client() as client:
        # make a request to the about page
        response = client.get('/download_files')

        # check that the response status code is 200 OK
        assert response.status_code == 200

        # check that the response data contains the expected text
        # assert b'This is the about page.' in response.data

