import instaloader

insta = instaloader.Instaloader()

acc = "instagram" #account id

insta.download_profile(acc, profile_pic_only=False)