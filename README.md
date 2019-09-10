# halloween_2019
Just a fun home automation to use a Raspberry Pi connected to a pi cam, servo, and LEDs to start recording video when motion is detected, turn on LED "eyes" and turn a styrofoam mannequin head with a Halloween mask on to follow a person's movement.   The videos will be broadcast on a website hosted on my own server.

# Bill of Materials
    # Electronics
        - Raspberry Pi
        - Micro SD
        - USB power supply
        - Pi Camera
        - servo
        - servo motor driver
        - red LEDs for eyes
        - red LEDs for back lighting
        - resistors
        - bread board
        - jumper wires

    # Pennywise
        - Pennywise the clown mask
        - white gloves
        - claw fingertips
        - ruffle collar
        - manequin head
        - prop eyes
        - red helium balloon
    
    # sewer
        - 2x4 boards
        - 1x2 boards
        - plywood
        - wood screws
        - white spray paint
        - black spray paint
        - copper acrylic paint
        - light gray acrylic paint



# TODO:  SET SECURITY ACROSS ALL COMMUNICATION METHODS!!!!
    # SECURITY FIRST SECURITY FIRST SECURITY FIRST
    # https://www.raspberrypi.org/documentation/configuration/security.md
# TODO:  Set up Pi as web server
    # https://www.makeuseof.com/tag/host-website-raspberry-pi/
    # https://www.raspberrypi.org/forums/viewtopic.php?t=235347
# TODO:  Install MySQL on db server
    # apt-get install mysql-server mysql-client
    # mysql_secure_installation
# TODO:  Set up database connection
    # https://devdocs.magento.com/guides/v2.3/install-gde/prereq/mysql_remote.html
# TODO:  set up website
# TODO:  write REST API to interact with website
# TODO:  set up CI/CD pipeline to Raspberry Pi
# TODO:  set up and interface with Raspberry Pi camera
    # https://www.youtube.com/watch?v=qk1IVs5B1GI
# TODO:  set up text messaging with pi and twilio
    # https://www.youtube.com/watch?v=Oi37lg_ciJ8
# TODO:  interface Pi with servo

# TODO:  interface with LEDs for eyes
    # https://www.youtube.com/watch?v=WLo5Rgvj6qo
# TODO:  set up object detection
    # https://www.youtube.com/watch?v=1I4gHpctXbU
    # https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/
        # set base frame
        # poll image detection every second
        # detect change greater than X percent of original image to represent motion
            # cv2 module

# facebook developer page
    # https://developers.facebook.com/docs/live-video-api/guides/streaming#broadcast-on-a-page

# fake api calls
    # https://jsonplaceholder.typicode.com


# App logic
    - Person approaches
        - Camera recognizes motion based on x percent difference in default image
        - Camera starts video
        # gopro section may be added if there is time
        - Pi try connection to GoPro
            - success
                - wakeup GoPro
                - Start video
            - exception
                - log exception
                - continue
        - Pi try camera video
            - success
                - turn on LED eyes
                - turn IT head with servo
                - follow movement
                - if movement stops
                    - wait 5 seconds
                    - stop video
                    - if GoPro
                        - stop GoPro
                        - store GoPro
                        - watch for exit 0
                            - trigger job to connect to GoPro from db server (not sure about this one)
                                - LOGIC TBD BASED ON STORY COMPLETION
                    - sftp pi video
                    - try confirm transfer to ftp server
                        - success
                            - delete video from pi
                            - log ftp file loc
                            - try store file loc in db
                                - success
                                    - try use API to send file to upload video to website
                                        - success
                                            - try send new video text via twilio (allow subscribers?)
                                                - success
                                                    - exit 0
                                                - exception
                                                    - log exception
                                                    - email twilio failure
                                                    - exit 1
                                        - exception
                                            - log exception
                                            - email API failure
                                            - exit 1
                                - exception
                                    - log exception
                                    - email db failure
                                    - exit 1
                        - exception
                            - log exception
                            - email file transer failure
                            - exit 1