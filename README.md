# Gimkit Strategy Calculator #
`calc-gimkit-strategy.py` is a Python script by [Noble H. Mushtak](https://noblemushtak.pythonanywhere.com/) which generates optimal strategies for the educational game [Gimkit](https://www.gimkit.com/). For example, here is the optimal strategy for going from $1 to over $4,000,000,000 and buying all Level 10 Gimkit upgrades except insurance in as few steps as possible (all steps which are not just answering a normal question are in bold):

1. Answer 1 question, bringing your total up to $2
2. Answer 1 question, bringing your total up to $5
3. Answer 1 question, bringing your total up to $8
4. Answer 1 question, bringing your total up to $11
5. Answer 1 question, bringing your total up to $14
6. Answer 1 question, bringing your total up to $17
7. **Buy the Level 2 ($20) streak bonus upgrade** for $15, making your total $2
8. Answer 1 question, bringing your total up to $23
9. Answer 1 question, bringing your total up to $44
10. Answer 1 question, bringing your total up to $65
11. Answer 1 question, bringing your total up to $86
12. Answer 1 question, bringing your total up to $107
13. **Buy the Level 3 ($50) money per question upgrade** for $100, making your total $7
14. Answer 1 question, bringing your total up to $77
15. **Buy the mega bonus** for $55, making your total $22
16. Answer 1 question, bringing your total up to $92
17. Answer 1 question, bringing your total up to $162
18. **Buy the Level 3 ($100) streak bonus upgrade** for $150, making your total $12
19. Answer 1 question, bringing your total up to $162
20. Answer 1 question, bringing your total up to $312
21. **Buy the Level 3 (2x) multiplier upgrade** for $300, making your total $12
22. Answer 1 question, bringing your total up to $312
23. **Buy and use the discounter** for $300, making your total $12
24. Answer 1 question, bringing your total up to $312
25. Answer 1 question, bringing your total up to $612
26. Answer 1 question, bringing your total up to $912
27. Answer 1 question, bringing your total up to $1212
28. **Buy the Level 4 ($200) streak bonus upgrade** for $1125, making your total $87
29. Answer 1 question, bringing your total up to $587
30. Answer 1 question, bringing your total up to $1087
31. Answer 1 question, bringing your total up to $1587
32. **Buy the Level 4 (3x) multiplier upgrade** for $1500, making your total $87
33. Answer 1 question, bringing your total up to $837
34. Answer 1 question, bringing your total up to $1587
35. Answer 1 question, bringing your total up to $2337
36. Answer 1 question, bringing your total up to $3087
37. Answer 1 question, bringing your total up to $3837
38. Answer 1 question, bringing your total up to $4587
39. Answer 1 question, bringing your total up to $5337
40. Answer 1 question, bringing your total up to $6087
41. Answer 1 question, bringing your total up to $6837
42. Answer 1 question, bringing your total up to $7587
43. **Buy the Level 5 ($500) money per question upgrade** for $7500, making your total $87
44. Answer 1 question, bringing your total up to $2187
45. Answer 1 question, bringing your total up to $4287
46. Answer 1 question, bringing your total up to $6387
47. Answer 1 question, bringing your total up to $8487
48. Answer 1 question, bringing your total up to $10587
49. Answer 1 question, bringing your total up to $12687
50. **Buy the Level 5 ($1000) streak bonus upgrade** for $11250, making your total $1437
51. **Buy the rebooter** for $1435, making your total $2
52. Answer 1 question, bringing your total up to $4502
53. Answer 1 question, bringing your total up to $9002
54. **Buy the Level 5 (5x) multiplier upgrade** for $9000, making your total $2
55. Answer 1 question, bringing your total up to $7502
56. Answer 1 question, bringing your total up to $15002
57. Answer 1 question, bringing your total up to $22502
58. Answer 1 question, bringing your total up to $30002
59. Answer 1 question, bringing your total up to $37502
60. Answer 1 question, bringing your total up to $45002
61. Answer 1 question, bringing your total up to $52502
62. Answer 1 question, bringing your total up to $60002
63. **Buy the Level 6 ($2000) money per question upgrade** for $56250, making your total $3752
64. Answer 1 question, bringing your total up to $18752
65. Answer 1 question, bringing your total up to $33752
66. Answer 1 question, bringing your total up to $48752
67. Answer 1 question, bringing your total up to $63752
68. **Buy the Level 6 (8x) multiplier upgrade** for $63750, making your total $2
69. Answer 1 question, bringing your total up to $24002
70. Answer 1 question, bringing your total up to $48002
71. Answer 1 question, bringing your total up to $72002
72. Answer 1 question, bringing your total up to $96002
73. **Buy the Level 6 ($4000) streak bonus upgrade** for $86250, making your total $9752
74. Answer 1 question, bringing your total up to $57752
75. Answer 1 question, bringing your total up to $105752
76. Answer 1 question, bringing your total up to $153752
77. Answer 1 question, bringing your total up to $201752
78. Answer 1 question, bringing your total up to $249752
79. Answer 1 question, bringing your total up to $297752
80. Answer 1 question, bringing your total up to $345752
81. **Buy the Level 7 ($10000) streak bonus upgrade** for $337500, making your total $8252
82. **Buy the mini bonus** for $270, making your total $7982
83. **Answer 1 question using the mini and mega bonuses**, bringing your total up to $967982
84. Answer 1 question, bringing your total up to $1063982
85. Answer 1 question, bringing your total up to $1159982
86. **Buy the Level 8 ($50000) streak bonus upgrade** for $1125000, making your total $34982
87. Answer 1 question, bringing your total up to $450982
88. Answer 1 question, bringing your total up to $866982
89. **Use the rebooter** to regenerate your previously bought powerups.
90. **Buy the Level 7 (12x) multiplier upgrade** for $525000, making your total $341982
91. **Answer 1 question using the mini and mega bonuses**, bringing your total up to $6581982
92. Answer 1 question, bringing your total up to $7205982
93. Answer 1 question, bringing your total up to $7829982
94. **Buy the Level 9 ($250000) money per question upgrade** for $7500000, making your total $329982
95. Answer 1 question, bringing your total up to $3929982
96. Answer 1 question, bringing your total up to $7529982
97. **Buy the Level 8 (18x) multiplier upgrade** for $4875000, making your total $2654982
98. Answer 1 question, bringing your total up to $8054982
99. Answer 1 question, bringing your total up to $13454982
100. **Buy the Level 9 ($1000000) streak bonus upgrade** for $11250000, making your total $2204982
101. Answer 1 question, bringing your total up to $24704982
102. Answer 1 question, bringing your total up to $47204982
103. Answer 1 question, bringing your total up to $69704982
104. **Buy the Level 9 (30x) multiplier upgrade** for $48750000, making your total $20954982
105. Answer 1 question, bringing your total up to $58454982
106. Answer 1 question, bringing your total up to $95954982
107. Answer 1 question, bringing your total up to $133454982
108. Answer 1 question, bringing your total up to $170954982
109. **Buy the Level 10 ($5000000) streak bonus upgrade** for $150000000, making your total $20954982
110. Answer 1 question, bringing your total up to $178454982
111. **Buy the Level 10 ($1000000) money per question upgrade** for $75000000, making your total $103454982
112. Answer 1 question, bringing your total up to $283454982
113. Answer 1 question, bringing your total up to $463454982
114. Answer 1 question, bringing your total up to $643454982
115. Answer 1 question, bringing your total up to $823454982
116. **Buy the Level 10 (100x) multiplier upgrade** for $750000000, making your total $73454982
117. Answer 1 question, bringing your total up to $673454982
118. Answer 1 question, bringing your total up to $1273454982
119. Answer 1 question, bringing your total up to $1873454982
120. Answer 1 question, bringing your total up to $2473454982
121. Answer 1 question, bringing your total up to $3073454982
122. Answer 1 question, bringing your total up to $3673454982
123. Answer 1 question, bringing your total up to $4273454982

Please note that neither this script nor its author are associated with the Gimkit company or any Gimkit employee in any way. I am simply a student who used Gimkit in high-school and wanted to calculate the optimal strategy for completing Gimkit assignments.

Documentation coming soon!