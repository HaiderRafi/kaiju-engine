# # final version
# import pandas as pd
# import re

# def generate_html_from_excel(template_html_file, excel_file, output_html_file):
#     # Load the Excel file
#     data = pd.read_excel(excel_file)

#     # Read the HTML template
#     with open(template_html_file, 'r', encoding='utf-8') as file:
#         html_template = file.read()

#     # Prepare placeholders for dynamic content
#     all_influencers_content = ""

#     # Update title, meta description, and canonical URL based on the first row
#     first_row = data.iloc[0]
#     title = first_row['title'] if pd.notna(first_row['title']) else 'Default Title'
#     meta_description = first_row['meta'] if pd.notna(first_row['meta']) else 'Default meta description'
#     canonical_url = first_row['canonical'] if pd.notna(first_row['canonical']) else 'https://default.url'
#     h1_title = first_row['h1'] if pd.notna(first_row['h1']) else 'Default H1 Title'
#     intro_paragraph = first_row['p'] if pd.notna(first_row['p']) else 'Default paragraph'
#     h2_title = first_row['h2'] if pd.notna(first_row['h2']) else 'Default H2 Title'

#     # Iterate over the rows of the Excel sheet and generate the influencer content
#     for index, row in data.iterrows():
#         # Create the influencer details list for each row
#         image = row['img'] if pd.notna(row['img']) else 'default_image.png'
#         rank = row['rank'] if pd.notna(row['rank']) else 'N/A'
#         name = row['name'] if pd.notna(row['name']) else 'Unknown'
#         user_url = row['user-url'] if pd.notna(row['user-url']) else '#'
#         user_name = row['user-name'] if pd.notna(row['user-name']) else 'Unknown'
#         followers = row['followers'] if pd.notna(row['followers']) else '0'
#         engagement = row['engagement'] if pd.notna(row['engagement']) else '0'
#         bio = row['bio'] if pd.notna(row['bio']) else 'No bio available'
#         # reel = row['reel'] if pd.notna(row['reel']) else 'No reel available'

#         # Construct the influencer profile
#         influencer_content = f"""
#         <div class="influencer-profile">
#             <div class="profile-header">
#                 <img class="profile-img" alt="{name}" src="{image}" />
#                 <div class="profile-info">
#                     <h3 class="profile-name">
#                         <span class="profile-rank">{rank}</span> {name} 
#                         <a href="{user_url}" target="_blank" rel="nofollow" class="profile-handle">{user_name}</a>
#                     </h3>
#                     <div class="profile-stats-grid">
#                         <div class="stat-item">
#                             <i class="fas fa-users stat-icon"></i>
#                             <span>Followers:</span> {followers}
#                         </div>
#                         <div class="stat-item">
#                             <i class="fas fa-chart-line stat-icon"></i>
#                             <span>Engagement Rate:</span> {engagement}
#                         </div>
#                         <div class="stat-item">
#                             <i class="fas fa-heart stat-icon"></i>
#                             <span>Bio:</span> {bio}
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#         """
#         # Append influencer content to the accumulated content
#         all_influencers_content += influencer_content

#     # Replace the placeholders in the HTML template for the title, meta, canonical URL, and h1
#     html_content = html_template.replace("<title></title>", f"<title>{title}</title>")
#     html_content = html_content.replace('<meta name="description" content="">', f'<meta name="description" content="{meta_description}">')
#     html_content = html_content.replace('<link rel="canonical" href="">', f'<link rel="canonical" href="{canonical_url}">')
#     html_content = html_content.replace("<h1></h1>", f"<h1>{h1_title}</h1>")
#     html_content = html_content.replace('<p class="intro-text"></p>', f'<p class="intro-text">{intro_paragraph}</p>')
#     html_content = html_content.replace("<h2></h2>", f"<h2>{h2_title}</h2>")

#     # Update the headline and description in the "schema"
#     html_content = html_content.replace('"headline": "Top 10 Video Production Companies in India"', f'"headline": "{title}"')
#     html_content = html_content.replace('"description": "Explore here list of top 10 video production companies in India, they craft high-quality videos that drive engagement & sales. List include- Vidzy, Grynow"', f'"description": "{meta_description}"')

#     # Use regex to remove the placeholder influencer profile div and insert dynamically generated profiles
#     html_content = re.sub(
#         r'<div class="influencer-profile">.*?</div>\s*</div>\s*</div>\s*</div>\s*</section>',
#         all_influencers_content + "</div>\n        </div>\n    </div>\n</section>",
#         html_content,
#         flags=re.DOTALL
#     )

#     # Replace the 'post-canonical-here' and 'date-here' placeholders in the schema
#     post_canonical = first_row['post-canonical-here'] if pd.notna(first_row['post-canonical-here']) else 'default-post-canonical'
#     date_here = str(first_row['date-here']) if pd.notna(first_row['date-here']) else 'default-date'
#     html_content = html_content.replace("post-canonical-here", post_canonical)
#     html_content = html_content.replace("date-here", date_here)

#     # Save the final accumulated content into one HTML file
#     with open(output_html_file, 'w', encoding='utf-8') as output:
#         output.write(html_content)
#     print(f"Generated combined HTML file: {output_html_file}")

# # Example usage
# template_html_file = 'template2.html'  # Path to your HTML template file
# excel_file = 'kaiju-sheet.xlsx'  # Reference to the Excel file in the same folder
# output_html_file = 'output_combined.html'  # The final HTML file that will contain all the content

# generate_html_from_excel(template_html_file, excel_file, output_html_file)


# -------------------------------------------------------------------------

# import pandas as pd

# def generate_influencer_html(template_html_file, excel_file, output_html_file):
#     # Load the Excel file
#     data = pd.read_excel(excel_file)

#     # Read the HTML template
#     with open(template_html_file, 'r', encoding='utf-8') as file:
#         html_template = file.read()

#     # Placeholder for influencer list content
#     influencer_content_list = ""

#     # Iterate over the rows in the Excel sheet and generate the influencer content
#     for index, row in data.iterrows():
#         # Extract influencer details from the Excel file
#         image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
#         profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
#         # rank = row['rank'] if pd.notna(row['rank']) else 'N/A'
#         name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
#         followers = row['Followers'] if pd.notna(row['Followers']) else '0'
#         engagement = row['Engagement'] if pd.notna(row['Engagement']) else '0'

#          # Dynamic rank generation (index starts at 0, so add 1 for ranking)
#         rank = index + 1

#         # Construct the HTML block for each influencer
#         influencer_html = f"""
#         <div class="influencer-profile">
#             <div class="profile-header">
#                 <img class="profile-img" alt="{name}" src="{image}" />
#                 <div class="profile-info">
#                     <div class="blog-profile-wrapper">
#                     <h3 class="profile-name"><span class="profile-rank">{rank}</span> {name} </h3>
#                     <a class="profile-btn" href="{profileUrl}">Get Contact <i class="fas fa-external-link-alt"></i></a>
#                 </div>
#                     <div class="profile-stats-grid">
#                         <div class="stat-item">
#                             <span>Followers:</span> {followers}
#                         </div>
#                         <div class="stat-item">
#                             <span>ER:</span> {engagement}
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#         """
#         influencer_content_list += influencer_html

#     # Replace placeholder in the HTML template with the generated influencer content
#     final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)


#     # Save the final HTML content into the output file
#     with open(output_html_file, 'w', encoding='utf-8') as output_file:
#         output_file.write(final_html_content)

#     print(f"HTML file '{output_html_file}' generated successfully.")

# # Example usage
# template_html_file = 'igy-template.html'  # Path to your updated HTML template file
# excel_file = 'top-hundred-Fashion-Influencers-in-uae.xlsx'  # Path to your Excel file
# output_html_file = 'output_influencers.html'  # Output HTML file

# generate_influencer_html(template_html_file, excel_file, output_html_file)




# --------------------------------------------------------------------------------
# working version for igy Grow with title meta updation

# import pandas as pd
# import random


# def generate_influencer_html(template_html_file, excel_file, output_html_file):
#     # Load the Excel file
#     data = pd.read_excel(excel_file)

#     # Read the HTML template
#     with open(template_html_file, 'r', encoding='utf-8') as file:
#         html_template = file.read()

#     # Get the Niche and Country from the first row of the Excel file
#     niche = data.loc[0, 'Nichee'] if pd.notna(data.loc[0, 'Nichee']) else 'Unknown Niche'
#     country = data.loc[0, 'Country'] if pd.notna(data.loc[0, 'Country']) else 'Unknown Country'

#     # Prepare the lowercase versions for Niche and Country
#     niche_lower = niche.lower()
#     country_lower = country.lower()

#        # List of words/phrases for randomization
#     random_phrases = [
#         "follower count", "content quality", "engagement rate", 
#         "audience trust", "sentiment analysis", "brand collaborations"
#     ]

#     # Shuffle the list and select a random subset (e.g., 3 items)
#     random.shuffle(random_phrases)
#     selected_phrases = random_phrases[:6]

#     # Join the selected phrases into a comma-separated string
#     prandom_var = ', '.join(selected_phrases)

#     # Replace the placeholders in the HTML template
#     html_template = html_template.replace('$NicheVar$', niche)
#     html_template = html_template.replace('$CountryVar$', country)
#     html_template = html_template.replace('$NicheVarC$', niche_lower)
#     html_template = html_template.replace('$CountryVarC$', country_lower)
#     html_template = html_template.replace('$PRandomVar$', prandom_var)

#     # Placeholder for influencer list content
#     influencer_content_list = ""

#     # Iterate over the rows in the Excel sheet and generate the influencer content
#     for index, row in data.iterrows():
#         # Extract influencer details from the Excel file
#         image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
#         profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
#         name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
#         followers = row['Followers'] if pd.notna(row['Followers']) else '0'
#         engagement = row['Engagement'] if pd.notna(row['Engagement']) else '0'

#         # Dynamic rank generation (index starts at 0, so add 1 for ranking)
#         rank = index + 1

#         # Construct the HTML block for each influencer
#         influencer_html = f"""
#         <div class="influencer-profile">
#             <div class="profile-header">
#                 <img class="profile-img" alt="{name}" src="{image}" />
#                 <div class="profile-info">
#                     <div class="blog-profile-wrapper">
#                     <h3 class="profile-name"><span class="profile-rank">{rank}</span> {name} </h3>
#                     <a class="profile-btn" href="{profileUrl}">Get Contact <i class="fas fa-external-link-alt"></i></a>
#                 </div>
#                     <div class="profile-stats-grid">
#                         <div class="stat-item">
#                             <span>Followers:</span> {followers}
#                         </div>
#                         <div class="stat-item">
#                             <span>ER:</span> {engagement}
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#         """
#         influencer_content_list += influencer_html

#     # Replace placeholder in the HTML template with the generated influencer content
#     final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)


#     # Save the final HTML content into the output file
#     with open(output_html_file, 'w', encoding='utf-8') as output_file:
#         output_file.write(final_html_content)

#     print(f"HTML file '{output_html_file}' generated successfully.")

# # Example usage
# template_html_file = 'igy-template.html'  # Path to your updated HTML template file
# excel_file = 'top-hundred-Fashion-Influencers-in-uae.xlsx'  # Path to your Excel file
# output_html_file = 'output_influencers.html'  # Output HTML file

# generate_influencer_html(template_html_file, excel_file, output_html_file)


# ---------------------------------------------------------------------------------------

# form is removing but additional is list is removed


# import pandas as pd
# import re

# def generate_influencer_html(template_html_file, excel_file, output_html_file):
#     # Load the Excel file
#     data = pd.read_excel(excel_file)

#     # Read the HTML template
#     with open(template_html_file, 'r', encoding='utf-8') as file:
#         html_template = file.read()

#     # Get the Niche and Country from the first row of the Excel file
#     niche = data.loc[0, 'Nichee'] if pd.notna(data.loc[0, 'Nichee']) else 'Unknown Niche'
#     country = data.loc[0, 'Country'] if pd.notna(data.loc[0, 'Country']) else 'Unknown Country'

#     # Prepare the lowercase versions for Niche and Country
#     niche_lower = niche.lower()
#     country_lower = country.lower()

#     # Replace the placeholders in the HTML template
#     html_template = html_template.replace('$NicheVar$', niche)
#     html_template = html_template.replace('$CountryVar$', country)
#     html_template = html_template.replace('$NicheVarC$', niche_lower)
#     html_template = html_template.replace('$CountryVarC$', country_lower)

#     # Placeholder for influencer list content
#     influencer_content_list = ""

#     # Iterate over the rows in the Excel sheet and generate the influencer content
#     for index, row in data.iterrows():
#         # Extract influencer details from the Excel file
#         image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
#         profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
#         name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
#         followers = row['Followers'] if pd.notna(row['Followers']) else '0'
#         engagement = row['Engagement'] if pd.notna(row['Engagement']) else '0'

#         # Dynamic rank generation (index starts at 0, so add 1 for ranking)
#         rank = index + 1

#         # Construct the HTML block for each influencer
#         influencer_html = f"""
#         <div class="influencer-profile">
#             <div class="profile-header">
#                 <img class="profile-img" alt="{name}" src="{image}" />
#                 <div class="profile-info">
#                     <div class="blog-profile-wrapper">
#                     <h3 class="profile-name"><span class="profile-rank">{rank}</span> {name} </h3>
#                     <a class="profile-btn" href="{profileUrl}">Get Contact <i class="fas fa-external-link-alt"></i></a>
#                 </div>
#                     <div class="profile-stats-grid">
#                         <div class="stat-item">
#                             <span>Followers:</span> {followers}
#                         </div>
#                         <div class="stat-item">
#                             <span>ER:</span> {engagement}
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#         """
#         influencer_content_list += influencer_html

#     # Replace placeholder in the HTML template with the generated influencer content
#     final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)

#     # Regex block to remove placeholder and replace with content
#     final_html_content = re.sub(
#         r'<div class="profile-header">\s*<!-- Profile Image -->\s*<img class="profile-img" alt="Virat Kohli" src="\.\./assets/blog/template/salmon\.png" />\s*<div class="profile-info">.*?</div>\s*</div>\s*</div>\s*</div>\s*</section>',
#         influencer_content_list + "</div>\n        </div>\n    </div>\n</section>",
#         final_html_content,
#         flags=re.DOTALL
#     )

#     # Save the final HTML content into the output file
#     with open(output_html_file, 'w', encoding='utf-8') as output_file:
#         output_file.write(final_html_content)

#     print(f"HTML file '{output_html_file}' generated successfully.")

# # Example usage
# template_html_file = 'igy-template.html'  # Path to your updated HTML template file
# excel_file = 'top-hundred-Fashion-Influencers-in-uae.xlsx'  # Path to your Excel file
# output_html_file = 'output_influencers.html'  # Output HTML file

# generate_influencer_html(template_html_file, excel_file, output_html_file)


# -----------------------------------------------------------------

#  perfect version
#  everything is changing:- 


# import pandas as pd
# import random


# def generate_influencer_html(template_html_file, excel_file, output_html_file):
    

#     # Load the Excel file
#     data = pd.read_excel(excel_file)

#     # Read the HTML template
#     with open(template_html_file, 'r', encoding='utf-8') as file:
#         html_template = file.read()

#     # Get the Niche and Country from the first row of the Excel file
#     niche = data.loc[0, 'Nichee'] if pd.notna(data.loc[0, 'Nichee']) else 'Unknown Niche'
#     country = data.loc[0, 'Country'] if pd.notna(data.loc[0, 'Country']) else 'Unknown Country'

#     # Prepare the lowercase versions for Niche and Country
#     niche_lower = niche.lower()
#     country_lower = country.lower()

#     # Replace the placeholders in the HTML template
#     html_template = html_template.replace('$NicheVar$', niche)
#     html_template = html_template.replace('$CountryVar$', country)
#     html_template = html_template.replace('$NicheVarC$', niche_lower)
#     html_template = html_template.replace('$CountryVarC$', country_lower)

#     # List of words to randomize for PRandomVar
#     random_words = ["follower count", "content quality", "engagement rate", "audience trust", 
#                     "sentiment analysis", "brand collaborations"]

#     # Randomly select words for PRandomVar and replace in template
#     prandom_var = ', '.join(random.sample(random_words, 6))  # Randomize 3 words
#     html_template = html_template.replace('$PRandomVar$', prandom_var)

#     # Remove the placeholder influencer block after populating 
#     placeholder_start = html_template.find('<div class="influencer-profile">')
#     placeholder_end = html_template.find('<!-- Additional influencer profiles can go here -->')

#     if placeholder_start != -1 and placeholder_end != -1:
#         html_template = html_template[:placeholder_start] + html_template[placeholder_end:]

#     # Placeholder for influencer list content
#     influencer_content_list = ""

#     # Iterate over the rows in the Excel sheet and generate the influencer content
#     for index, row in data.iterrows():
#         # Extract influencer details from the Excel file
#         image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
#         profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
#         name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
#         followers = row['Followers'] if pd.notna(row['Followers']) else '0'
#         engagement = row['Engagement'] if pd.notna(row['Engagement']) else '0'

#         # Dynamic rank generation (index starts at 0, so add 1 for ranking)
#         rank = index + 1

#         # Construct the HTML block for each influencer
#         influencer_html = f"""
#         <div class="influencer-profile">
#             <div class="profile-header">
#                 <img class="profile-img" alt="{name}" src="{image}" />
#                 <div class="profile-info">
#                     <div class="blog-profile-wrapper">
#                     <h3 class="profile-name"><span class="profile-rank">{rank}</span> {name} </h3>
#                     <a class="profile-btn" href="{profileUrl}">Get Contact <i class="fas fa-external-link-alt"></i></a>
#                 </div>
#                     <div class="profile-stats-grid">
#                         <div class="stat-item">
#                             <span>Followers:</span> {followers}
#                         </div>
#                         <div class="stat-item">
#                             <span>ER:</span> {engagement}
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#         """
#         influencer_content_list += influencer_html

#     # Replace placeholder in the HTML template with the generated influencer content
#     final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)

#     # Save the final HTML content into the output file
#     with open(output_html_file, 'w', encoding='utf-8') as output_file:
#         output_file.write(final_html_content)

#     print(f"HTML file '{output_html_file}' generated successfully.")


# # Example usage
# template_html_file = 'igy-template.html'  # Path to your updated HTML template file
# excel_file = 'top-hundred-Fashion-Influencers-in-uae.xlsx'  # Path to your Excel file
# output_html_file = 'best-{niche_lower}-influencers-in-{country_lower}.html'  # Output HTML file

# generate_influencer_html(template_html_file, excel_file, output_html_file)













# ----------------------------------------------------------------------------------------
# note:- auto file name is not working
# final version for IGY grow


# import pandas as pd
# import random


# def generate_influencer_html(template_html_file, excel_file, output_html_file):
#     # Load the Excel file
#     data = pd.read_excel(excel_file)

#     # Read the HTML template
#     with open(template_html_file, 'r', encoding='utf-8') as file:
#         html_template = file.read()

#     # Get the Niche and Country from the first row of the Excel file
#     niche = data.loc[0, 'Nichee'] if pd.notna(data.loc[0, 'Nichee']) else 'Unknown Niche'
#     country = data.loc[0, 'Country'] if pd.notna(data.loc[0, 'Country']) else 'Unknown Country'

#     # Prepare the lowercase versions for Niche and Country
#     niche_lower = niche.lower()
#     country_lower = country.lower()

#     # Replace the placeholders in the HTML template
#     html_template = html_template.replace('$NicheVar$', niche)
#     html_template = html_template.replace('$CountryVar$', country)
#     html_template = html_template.replace('$NicheVarC$', niche_lower)
#     html_template = html_template.replace('$CountryVarC$', country_lower)

#     # List of words to randomize for PRandomVar
#     random_words = ["follower count", "content quality", "engagement rate", "audience trust", 
#                     "sentiment analysis", "brand collaborations"]

#     # Randomly select words for PRandomVar and replace in template
#     prandom_var = ', '.join(random.sample(random_words, 6))  # Randomize 6 words
#     html_template = html_template.replace('$PRandomVar$', prandom_var)

#     # Remove the placeholder influencer block after populating 
#     placeholder_start = html_template.find('<div class="influencer-profile">')
#     placeholder_end = html_template.find('<!-- Additional influencer profiles can go here -->')

#     if placeholder_start != -1 and placeholder_end != -1:
#         html_template = html_template[:placeholder_start] + html_template[placeholder_end:]

#     # Placeholder for influencer list content
#     influencer_content_list = ""

#     # Iterate over the rows in the Excel sheet and generate the influencer content
#     for index, row in data.iterrows():
#         # Extract influencer details from the Excel file
#         image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
#         profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
#         name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
#         followers = row['Followers'] if pd.notna(row['Followers']) else '0'
#         avgLikes = row['Average-Likes'] if pd.notna(row['Average-Likes']) else '0'
#         engagement = row['Engagement'] if pd.notna(row['Engagement']) else '0'
#         male = row['Male'] if pd.notna(row['Male']) else 'Unknown'
#         female = row['Female'] if pd.notna(row['Female']) else 'Unknown'
#         reelPlays = row['Reel-Plays'] if pd.notna(row['Reel-Plays']) else '0'
#         # avgViews = row['Average-View'] if pd.notna(row['Average-View']) else '0'
        

#         # Dynamic rank generation (index starts at 0, so add 1 for ranking)
#         rank = index + 1

#         # Construct the HTML block for each influencer
#         influencer_html = f"""
#        <div class="influencer-profile">
#             <div class="profile-header">
#                 <img class="profile-img" alt="{name}" src="{image}" />
#                 <div class="profile-info">
#                     <div class="blog-profile-wrapper">
#                         <h3 class="profile-name"><span class="profile-rank">{rank}.</span> <a href="{profileUrl}" target="_blank">{name} </a> </h3>
#                         <p><i class="fa fa-instagram"></i><span>{followers}</span> Followers</p>
#                     </div>

#                     <div class="stats-block">
#                         <div class="stats-wrapper">
#                             <div class="stat-item">
#                                 <span>Engagement Rate: </span> {engagement}
#                             </div>
#                             <div class="stat-item">
#                                 <span>Avg Reel Plays: </span> {reelPlays}
#                             </div>
#                             <div class="stat-item">
#                                 <span>Avg <br> Likes: </span> {avgLikes}
#                             </div>
#                         </div>

#                         <div class="profile-stats-grid">
#                             <div class="stat-item">
#                                 <span>Male Audience: </span> {male}
#                             </div>
#                             <div class="stat-item">
#                                 <span>Female Audience: </span> {female}
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#         """
#         influencer_content_list += influencer_html

#     # Replace placeholder in the HTML template with the generated influencer content
#     final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)

#     # Save the final HTML content into the output file
#     with open(output_html_file, 'w', encoding='utf-8') as output_file:
#         output_file.write(final_html_content)

#     print(f"HTML file '{output_html_file}' generated successfully.")


# # Example usage
# template_html_file = 'igy-latest-template.html'  # Path to your updated HTML template file
# excel_file = 'igy-lifestyle-uae-new.xlsx'  # Path to your Excel file

# # Using f-string to create dynamic output file name
# niche_lower = 'lifestyle'  # You can extract this from your Excel or use as variable
# country_lower = 'uae'    # You can extract this from your Excel or use as variable
# output_html_file = f'best-{niche_lower}-influencers-in-{country_lower}.html'  # Dynamic output HTML file name

# generate_influencer_html(template_html_file, excel_file, output_html_file)








# ---------------------------------------------------------------------------------------





# version of missing fields
# working
# import pandas as pd
# import random


# def convert_to_number(value):
#     """Converts 'k' or 'M' formatted string to a number."""
#     if isinstance(value, str):
#         value = value.lower()  # Convert to lowercase to handle both 'K' and 'M'
#         if value.endswith('k'):
#             return float(value[:-1]) * 1_000
#         elif value.endswith('m'):
#             return float(value[:-1]) * 1_000_000
#     return float(value)


# def generate_influencer_html(template_html_file, excel_file, output_html_file):
#     # Load the Excel file
#     data = pd.read_excel(excel_file)

#     # Read the HTML template
#     with open(template_html_file, 'r', encoding='utf-8') as file:
#         html_template = file.read()

#     # Get the Niche and Country from the first row of the Excel file
#     niche = data.loc[0, 'Nichee'] if pd.notna(data.loc[0, 'Nichee']) else 'Unknown Niche'
#     country = data.loc[0, 'Country'] if pd.notna(data.loc[0, 'Country']) else 'Unknown Country'

#     # Prepare the lowercase versions for Niche and Country
#     niche_lower = niche.lower()
#     country_lower = country.lower()

#     # Replace the placeholders in the HTML template
#     html_template = html_template.replace('$NicheVar$', niche)
#     html_template = html_template.replace('$CountryVar$', country)
#     html_template = html_template.replace('$NicheVarC$', niche_lower)
#     html_template = html_template.replace('$CountryVarC$', country_lower)

#     # List of words to randomize for PRandomVar
#     random_words = ["follower count", "content quality", "engagement rate", "audience trust",
#                     "sentiment analysis", "brand collaborations"]

#     # Randomly select words for PRandomVar and replace in template
#     prandom_var = ', '.join(random.sample(random_words, 6))  # Randomize 6 words
#     html_template = html_template.replace('$PRandomVar$', prandom_var)

#     # Remove the placeholder influencer block after populating
#     placeholder_start = html_template.find('<div class="influencer-profile">')
#     placeholder_end = html_template.find('<!-- Additional influencer profiles can go here -->')

#     if placeholder_start != -1 and placeholder_end != -1:
#         html_template = html_template[:placeholder_start] + html_template[placeholder_end:]

#     # Placeholder for influencer list content
#     influencer_content_list = ""

#     # Iterate over the rows in the Excel sheet and generate the influencer content
#     for index, row in data.iterrows():
#         # Extract influencer details from the Excel file
#         image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
#         profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
#         name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
#         followers = row['Followers'] if pd.notna(row['Followers']) else '0'
#         avgLikes = row['Average-Likes'] if pd.notna(row['Average-Likes']) else '0'
#         female = row['Female'] if pd.notna(row['Female']) else 'Unknown'
#         reelPlays = row['Reel-Plays'] if pd.notna(row['Reel-Plays']) else '0'

#         # Convert followers, avgLikes, reelPlays to numeric values
#         followers_num = convert_to_number(followers)
#         avgLikes_num = convert_to_number(avgLikes)
#         reelPlays_num = convert_to_number(reelPlays)

#         # Calculate missing fields
#         if followers_num > 0:
#             engagement_rate = (avgLikes_num / followers_num) * 100
#             avg_views = (reelPlays_num / followers_num) * 100
#         else:
#             engagement_rate = 0
#             avg_views = 0

#         male_percentage = 100 - float(female.replace('%', '').strip()) if female != 'Unknown' else 'Unknown'


#         # Dynamic rank generation (index starts at 0, so add 1 for ranking)
#         rank = index + 1

#         # Construct the HTML block for each influencer
#         influencer_html = f"""
#         <div class="influencer-profile">
#             <div class="profile-header">
#                 <img class="profile-img" alt="{name}" src="{image}" />
#                 <div class="profile-info">
#                     <div class="blog-profile-wrapper">
#                     <h3 class="profile-name"><span class="profile-rank">{rank}.</span> {name} </h3>
#                     <a class="profile-btn" href="{profileUrl}">Get Contact <i class="fas fa-external-link-alt"></i></a>
#                 </div>
#                     <div class="profile-stats-grid">
#                         <div class="stat-item">
#                             <span>Followers:</span> {followers}
#                         </div>

#                         <div class="stat-item">
#                             <span>Average Likes: </span> {avgLikes}
#                         </div>

#                         <div class="stat-item">
#                             <span>Engagement Rate:</span> {engagement_rate:.2f}%
#                         </div>

#                          <div class="stat-item">
#                              <span>Male Percentage: </span> {male_percentage if male_percentage == 'Unknown' else f'{male_percentage:.2f}'}%
#                         </div>

#                         <div class="stat-item">
#                             <span>Female Percentage: </span> {female if female != 'Unknown' else 'Unknown'}
#                         </div>

#                         <div class="stat-item">
#                             <span>Reel Plays: </span> {reelPlays}
#                         </div>

#                         <div class="stat-item">
#                             <span>Average Views: </span> {avg_views:.2f}%
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#         """
#         influencer_content_list += influencer_html

#     # Replace placeholder in the HTML template with the generated influencer content
#     final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)

#     # Save the final HTML content into the output file
#     with open(output_html_file, 'w', encoding='utf-8') as output_file:
#         output_file.write(final_html_content)

#     print(f"HTML file '{output_html_file}' generated successfully.")


# # Example usage
# template_html_file = 'igy-blog-template-new.html'  # Path to your updated HTML template file
# excel_file = 'Main-Listicle-Sheet-Test.xlsx'  # Path to your Excel file

# # Using f-string to create dynamic output file name
# niche_lower = 'lifestyle'  # You can extract this from your Excel or use as variable
# country_lower = 'uae'    # You can extract this from your Excel or use as variable
# output_html_file = f'best-{niche_lower}-influencers-in-{country_lower}.html'  # Dynamic output HTML file name

# generate_influencer_html(template_html_file, excel_file, output_html_file)


















# ------------------------------------------------------------------------
# if male else female version
# working fine
# reel plays is commented
# 4 in line template

# import pandas as pd
# import random


# # convert k and m into decimal
# def convert_to_number(value):
#     """Converts 'k' or 'M' formatted string to a number."""
#     if isinstance(value, str):
#         value = value.lower()  # Convert to lowercase to handle both 'K' and 'M'
#         if value.endswith('k'):
#             return float(value[:-1]) * 1_000
#         elif value.endswith('m'):
#             return float(value[:-1]) * 1_000_000
#     return float(value)

# # def calculate_gender_percentage(row):
# #     """Calculates missing gender percentage dynamically based on provided input (either Male or Female)."""
# #     if pd.notna(row['Female']) and row['Female'] != 'Unknown':
# #         female_percentage = float(row['Female'].replace('%', '').strip())
# #         male_percentage = 100 - female_percentage
# #     elif pd.notna(row['Male']) and row['Male'] != 'Unknown':
# #         male_percentage = float(row['Male'].replace('%', '').strip())
# #         female_percentage = 100 - male_percentage
# #     else:
# #         female_percentage = 'Unknown'
# #         male_percentage = 'Unknown'

# #     return male_percentage, female_percentage


# # calculate missing gender male or female both
# def calculate_gender_percentage(row):
#     """Calculates missing gender percentage dynamically based on provided input (either Male or Female)."""
#     female_percentage = 'Unknown'
#     male_percentage = 'Unknown'
    
#     # Check if 'Female' column exists
#     if 'Female' in row.index and pd.notna(row['Female']) and row['Female'] != 'Unknown':
#         female_percentage = float(row['Female'].replace('%', '').strip())
#         male_percentage = 100 - female_percentage
#     # Check if 'Male' column exists
#     elif 'Male' in row.index and pd.notna(row['Male']) and row['Male'] != 'Unknown':
#         male_percentage = float(row['Male'].replace('%', '').strip())
#         female_percentage = 100 - male_percentage

#     return male_percentage, female_percentage

# def generate_influencer_html(template_html_file, excel_file, output_html_file):
#     # Load the Excel file
#     data = pd.read_excel(excel_file)

#     # Read the HTML template
#     with open(template_html_file, 'r', encoding='utf-8') as file:
#         html_template = file.read()

#     # Get the Niche and Country from the first row of the Excel file
#     niche = data.loc[0, 'Nichee'] if pd.notna(data.loc[0, 'Nichee']) else 'Unknown Niche'
#     country = data.loc[0, 'Country'] if pd.notna(data.loc[0, 'Country']) else 'Unknown Country'

#     # Prepare the lowercase versions for Niche and Country
#     niche_lower = niche.lower()
#     country_lower = country.lower()

#     # Replace the placeholders in the HTML template
#     html_template = html_template.replace('$NicheVar$', niche)
#     html_template = html_template.replace('$CountryVar$', country)
#     html_template = html_template.replace('$NicheVarC$', niche_lower)
#     html_template = html_template.replace('$CountryVarC$', country_lower)

#     # List of words to randomize for PRandomVar
#     random_words = ["follower count", "content quality", "engagement rate", "audience trust",
#                     "sentiment analysis", "brand collaborations"]

#     # Randomly select words for PRandomVar and replace in template
#     prandom_var = ', '.join(random.sample(random_words, 6))  # Randomize 6 words
#     html_template = html_template.replace('$PRandomVar$', prandom_var)

#     # Remove the placeholder influencer block after populating
#     placeholder_start = html_template.find('<div class="influencer-profile">')
#     placeholder_end = html_template.find('<!-- Additional influencer profiles can go here -->')

#     if placeholder_start != -1 and placeholder_end != -1:
#         html_template = html_template[:placeholder_start] + html_template[placeholder_end:]

#     # Placeholder for influencer list content
#     influencer_content_list = ""

#     # Iterate over the rows in the Excel sheet and generate the influencer content
#     for index, row in data.iterrows():
#         # Extract influencer details from the Excel file
#         image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
#         profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
#         name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
#         followers = row['Followers'] if pd.notna(row['Followers']) else '0'
#         avgLikes = row['Average-Likes'] if pd.notna(row['Average-Likes']) else '0'
#         # reelPlays = row['Reel-Plays'] if pd.notna(row['Reel-Plays']) else '0'

#         # Convert followers, avgLikes, reelPlays to numeric values
#         followers_num = convert_to_number(followers)
#         avgLikes_num = convert_to_number(avgLikes)
#         # reelPlays_num = convert_to_number(reelPlays)

#         # Calculate missing fields
#         if followers_num > 0:
#             engagement_rate = (avgLikes_num / followers_num) * 100
#             # avg_views = (reelPlays_num / followers_num) * 100
#         else:
#             engagement_rate = 0
#             avg_views = 0

#         # Calculate Male and Female percentages dynamically
#         male_percentage, female_percentage = calculate_gender_percentage(row)

#         # Dynamic rank generation (index starts at 0, so add 1 for ranking)
#         rank = index + 1

#         # Construct the HTML block for each influencer
#         influencer_html = f"""
#          <div class="influencer-profile">
#             <div class="profile-header">
#         <img class="profile-img" alt="{name}" src="{image}" />
#         <div class="profile-info">
#             <div class="blog-profile-wrapper">
#                 <h3 class="profile-name"><span class="profile-rank">{rank}.</span> <a href="{profileUrl}" target="_blank">{name}</a></h3>
#                 <p><i class="fab fa-instagram"></i><span>{followers}</span> Followers</p>
#             </div>

#             <div class="stats-block">
#                 <div class="stats-wrapper">
#                     <div class="stat-item">
#                         <span>Engagement Rate: </span> {engagement_rate:.2f}%
#                     </div>
#                     <div class="stat-item">
#                         <span class="stats-padd-right">Avg <br> Likes: </span> {avgLikes}
#                     </div>
#                     <div class="stat-item">
#                         <span>Male Audience: </span> {male_percentage if male_percentage == 'Unknown' else f'{male_percentage:.2f}'}%
#                     </div>
#                     <div class="stat-item">
#                         <span>Female Audience: </span> {female_percentage if female_percentage == 'Unknown' else f'{female_percentage:.2f}'}%
#                     </div>
#                 </div>
#             </div>
#         </div>
#     </div>
# </div>
#      """
#         influencer_content_list += influencer_html

#     # Replace placeholder in the HTML template with the generated influencer content
#     final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)

#     # Save the final HTML content into the output file
#     with open(output_html_file, 'w', encoding='utf-8') as output_file:
#         output_file.write(final_html_content)

#     print(f"HTML file '{output_html_file}' generated successfully.")

# # Example usage
# template_html_file = 'igy-latest-template.html'  # Path to your updated HTML template file
# excel_file = 'igy-home-decor-40.xlsx'  # Path to your Excel file

# # Using f-string to create dynamic output file name
# niche_lower = 'home-decor'  # You can extract this from your Excel or use as variable
# country_lower = 'uae'    # You can extract this from your Excel or use as variable
# output_html_file = f'best-{niche_lower}-influencers-in-{country_lower}.html'  # Dynamic output HTML file name

# generate_influencer_html(template_html_file, excel_file, output_html_file)

























# ---------------------------------------------------------------------
# randomise the list version
# working fine


import pandas as pd
import random

# Function to convert 'k' and 'M' values to numbers
def convert_to_number(value):
    """Converts 'k' or 'M' formatted string to a number."""
    if isinstance(value, str):
        value = value.lower()
        if value.endswith('k'):
            return float(value[:-1]) * 1_000
        elif value.endswith('m'):
            return float(value[:-1]) * 1_000_000
    return float(value)

# Calculate male and female percentages
def calculate_gender_percentage(row):
    """Calculates missing gender percentage dynamically based on provided input (either Male or Female)."""
    female_percentage = 'Unknown'
    male_percentage = 'Unknown'
    
    if 'Female' in row.index and pd.notna(row['Female']) and row['Female'] != 'Unknown':
        female_percentage = float(row['Female'].replace('%', '').strip())
        male_percentage = 100 - female_percentage
    elif 'Male' in row.index and pd.notna(row['Male']) and row['Male'] != 'Unknown':
        male_percentage = float(row['Male'].replace('%', '').strip())
        female_percentage = 100 - male_percentage

    return male_percentage, female_percentage

def generate_influencer_html(template_html_file, excel_file, output_html_file):
    # Load the Excel file
    data = pd.read_excel(excel_file)

    # Read the HTML template
    with open(template_html_file, 'r', encoding='utf-8') as file:
        html_template = file.read()

    # Get the Niche and Country from the first row of the Excel file
    niche = data.loc[0, 'Nichee'] if pd.notna(data.loc[0, 'Nichee']) else 'Unknown Niche'
    country = data.loc[0, 'Country'] if pd.notna(data.loc[0, 'Country']) else 'Unknown Country'

    # Prepare the lowercase versions for Niche and Country
    niche_lower = niche.lower()
    country_lower = country.lower()

    # Replace the placeholders in the HTML template
    html_template = html_template.replace('$NicheVar$', niche)
    html_template = html_template.replace('$CountryVar$', country)
    html_template = html_template.replace('$NicheVarC$', niche_lower)
    html_template = html_template.replace('$CountryVarC$', country_lower)

    # List of words to randomize for PRandomVar
    random_words = ["follower count", "content quality", "engagement rate", "audience trust",
                    "sentiment analysis", "brand collaborations"]

    # Randomly select words for PRandomVar and replace in template
    prandom_var = ', '.join(random.sample(random_words, 6))  # Randomize 6 words
    html_template = html_template.replace('$PRandomVar$', prandom_var)

    # Remove the placeholder influencer block after populating
    placeholder_start = html_template.find('<div class="influencer-profile">')
    placeholder_end = html_template.find('<!-- Additional influencer profiles can go here -->')

    if placeholder_start != -1 and placeholder_end != -1:
        html_template = html_template[:placeholder_start] + html_template[placeholder_end:]

    # Placeholder for influencer list content
    influencer_content_list = ""

    # Shuffle influencers in chunks of 10 randomly
    chunk_size = 10
    total_influencers = len(data)

    # Split influencers into chunks of 10
    chunks = [data[i:i + chunk_size] for i in range(0, total_influencers, chunk_size)]

    # Initialize rank counter
    rank = 1
    
    # Randomize the order within each chunk and process influencers
    for chunk in chunks:
        shuffled_chunk = chunk.sample(frac=1).reset_index(drop=True)  # Shuffle the chunk
        for _, row in shuffled_chunk.iterrows():
            # Extract influencer details from the Excel file
            image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
            profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
            name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
            followers = row['Followers'] if pd.notna(row['Followers']) else '0'
            avgLikes = row['Average-Likes'] if pd.notna(row['Average-Likes']) else '0'

            # Convert followers and avgLikes to numeric values
            followers_num = convert_to_number(followers)
            avgLikes_num = convert_to_number(avgLikes)

            # Calculate missing fields
            if followers_num > 0:
                engagement_rate = (avgLikes_num / followers_num) * 100
            else:
                engagement_rate = 0

            # Calculate Male and Female percentages dynamically
            male_percentage, female_percentage = calculate_gender_percentage(row)

            # Construct the HTML block for each influencer with correct rank
            influencer_html = f"""
            <div class="influencer-profile">
                <div class="profile-header">
            <img class="profile-img" alt="{name}" src="{image}" />
            <div class="profile-info">
                <div class="blog-profile-wrapper">
                    <h3 class="profile-name"><span class="profile-rank">{rank}.</span> <a href="{profileUrl}" target="_blank">{name}</a></h3>
                    <p><i class="fab fa-instagram"></i><span>{followers}</span> Followers</p>
                </div>

                <div class="stats-block">
                    <div class="stats-wrapper">
                        <div class="stat-item">
                            <span>Engagement Rate: </span> {engagement_rate:.2f}%
                        </div>
                        <div class="stat-item">
                            <span class="stats-padd-right">Avg <br> Likes: </span> {avgLikes}
                        </div>
                        <div class="stat-item">
                            <span>Male Audience: </span> {male_percentage if male_percentage == 'Unknown' else f'{male_percentage:.2f}'}%
                        </div>
                        <div class="stat-item">
                            <span>Female Audience: </span> {female_percentage if female_percentage == 'Unknown' else f'{female_percentage:.2f}'}%
                        </div>
                    </div>
                </div>
            </div>
            </div>
        </div>
        """
            influencer_content_list += influencer_html
            rank += 1  # Increment the rank for the next influencer

    # Replace placeholder in the HTML template with the generated influencer content
    final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)

    # Save the final HTML content into the output file
    with open(output_html_file, 'w', encoding='utf-8') as output_file:
        output_file.write(final_html_content)

    print(f"HTML file '{output_html_file}' generated successfully.")

# Example usage
template_html_file = 'igy-latest-template.html'  # Path to your updated HTML template file
excel_file = 'igy-food.xlsx'  # Path to your Excel file

niche_lower = 'food'  # You can extract this from your Excel or use as variable
country_lower = 'uae'    # You can extract this from your Excel or use as variable
output_html_file = f'best-{niche_lower}-influencers-in-{country_lower}.html'  # Dynamic output HTML file name

generate_influencer_html(template_html_file, excel_file, output_html_file)
