"""!
@brief Example 18
@details: Video feature extraction example
@author Theodoros Giannakopoulos {tyiannak@gmail.com}
"""
import video_features as vf

v = vf.VideoFeatureExtractor(["flow"], resize_width=300,
                             step = 0.25)
f, t, fn = v.extract_features("f1.mkv")
print(f.shape)
print(t.shape)
print(len(fn))
