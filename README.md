# Vendor-managment-assestment
# Setps to setup this repo

1. Clone this repo
   
       git clone https://github.com/hackdavid/Vendor-managment-assestment.git

<br>
2. Install the all requiremetns or package need for this repo

    pip install -r requirements.txt

3. Go to the directory 'Vendor-managment-assestm'

       cd Vendor-managment-assestm

4. Commands to run the application

       python manage.py runserver

Note: you can also create your own virtualenv for this repo so use below step if you want to use virtualeven

step1. install virtualenv library if not install in your system

    pip install virtualenv

step2. create virtualenv 

    virtualenv envs

step3. activate virtualenv

    source envs/scripts/activate

step4. install all the requiremnts now

    pip install -r requirements.txt

step5. go to project directory

    cd Vendor-managment-assestm

step6. Run the below command to start local server

    python manage.py runserver


# Note:
i had implemented this repo with TokenAuthentication but for developing , i had comment that line so if you want to use token base authentication 
uncomment the line inside each viewset of view.py



