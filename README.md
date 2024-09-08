## ImageFlow 
• ImageFlow is an automated image processing pipeline designed to download images according to user-defined keywords.
It then converts these images to grayscale and scales them to a specified size.
• Once processed, ImageFlow compiles the images into a zipped file and delivers them via email to the user.
• The project integrates Python scripting with external APIs to streamline image management and delivery

to run this
## python your_script_name.py --num_images NUM_IMAGES --keywords "KEYWORDS" --scale_percentage SCALE_PERCENTAGE --receiver_email RECEIVER_EMAIL
eg
## python main.py --num_images 10 --keywords "nature" --scale_percentage "50%" --receiver_email "example@example.com"
