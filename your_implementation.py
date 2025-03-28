# ************************************************************************************#
#                                                                                     #
#   Digiteq Automotive Python Hackathon                     :::::::::        :::      #
#   your_implementation.py                                 :+:    :+:     :+: :+:     #
#                                                         +:+    +:+    +:+   +:+     #
#   By: Roman Alexandrov <r.aleksandroff@gmail.com>      +#++:++#:    +#++:++#++:     #
#                                                       +#+    +#+   +#+     +#+      #
#   Created: 2025/03/27                                #+#    #+#   #+#     #+#       #
#   Updated: 2025/03/28                               ###    ###   ###     ###        #
#                                                                                     #
# ************************************************************************************#


import cv2
import numpy as np
import os

def classify_emoji(cropped):
    h, w = cropped.shape
    edges = cv2.Canny(cropped, 50, 150)
    top_half = edges[:h//2, :]
    bottom_half = edges[h//2:, :]
    top_count = np.count_nonzero(top_half)
    bottom_count = np.count_nonzero(bottom_half)
    
    if bottom_count > top_count * 1.5:
        return "happy"
    elif bottom_count < top_count * 0.8:
        return "sad"
    elif bottom_count > top_count and bottom_count < top_count * 1.2:
        return "surprised"
    else:
        if np.mean(cropped) < 128:
            return "angry"
        else:
            return "crying"

def loop_main():
    try:
        folder_path = "data/train/dataset/"     # modify to use different datasets
        image_prefix = "emoji_"
        image_suffix = ".jpg"
        image_range = range(1121)
    
        for i in image_range:
            image_name = f"{image_prefix}{i}{image_suffix}"
            image_path = os.path.join(folder_path, image_name)
        
            if not os.path.exists(image_path):
                continue
        
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
        
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            emoji_positions = [cv2.boundingRect(contour) for contour in contours]
            emoji_positions.sort(key=lambda b: b[1])
        
            merged_emojis = []
            threshold = 20  # Distance threshold to merge parts of the same emoji
        
            for x, y, w, h in emoji_positions:
                merged = False
                for i, (mx, my, mw, mh) in enumerate(merged_emojis):
                    if abs(mx - x) < threshold and abs(my - y) < threshold:
                        merged_emojis[i] = (min(mx, x), min(my, y), max(mx+mw, x+w) - min(mx, x), max(my+mh, y+h) - min(my, y))
                        merged = True
                        break
                if not merged:
                    merged_emojis.append((x, y, w, h))
        
            filtered_emojis = []
            distance_threshold = 10
            for x, y, w, h in merged_emojis:
                if not any(abs(x - fx) < distance_threshold and abs(y - fy) < distance_threshold for fx, fy, _, _ in filtered_emojis):
                    filtered_emojis.append((x, y, w, h))
        
            classified_emojis = [(x, y, classify_emoji(gray[y:y+h, x:x+w])) for x, y, w, h in filtered_emojis]
        
            print(f"Picture: {image_name}")
            for x, y, emoji_type in classified_emojis:
                print(f"Emoji: {emoji_type} Coordinates: ({x}, {y})")

    except Exception as e:
        print(f"Picture: emoji_{i}.jpg\nFAILURE: {str(e)}")

def implementation_main():
    loop_main()

if __name__ == "__main__":
    implementation_main()