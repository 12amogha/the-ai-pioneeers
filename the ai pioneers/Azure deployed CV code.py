
import cv2

# Load the two images
img1 = cv2.imread("C:\\Users\\subra\\Downloads\\dom1.jpg")
img2 = cv2.imread("C:\\Users\\subra\\Downloads\\dom2.jpg")

# Convert the images to grayscale
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Detect keypoints and extract local invariant descriptors using ORB
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1_gray, None)
kp2, des2 = orb.detectAndCompute(img2_gray, None)

# Match the descriptors using BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Sort the matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Calculate the percentage match
percentage_match = (len(matches) / len(kp1)) * 100
print("Percentage match: {:.2f}%".format(percentage_match))

# Draw the matches on the images
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Show the image with the matches
cv2.imshow("Matches", img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()
