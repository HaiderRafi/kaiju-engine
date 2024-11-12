# note:- auto file name is not working

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

#        # Construct dynamic output file name based on niche and country extracted from Excel
#     # output_html_file = f'best-{niche_lower}-influencers-in-{country_lower}.html'

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
#         avgViews = row['Average-View'] if pd.notna(row['Average-View']) else '0'

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
#                     <a class="profile-btn" href="{profileUrl}" target="_blank">View Profile <i class="fas fa-external-link-alt"></i></a>
#                 </div>
#                     <div class="profile-stats-grid">
#                         <div class="stat-item">
#                             <span>Followers: </span> {followers}
#                         </div>
#                             <div class="stat-item">
#                             <span>Average Likes: </span> {avgLikes}
#                         </div>

#                         <div class="stat-item">
#                             <span>Engagement Rate:</span> {engagement}
#                         </div>

#                          <div class="stat-item">
#                              <span>Male Audience: </span> {male}
#                         </div>

#                         <div class="stat-item">
#                             <span>Female Audience: </span> {female }
#                         </div>

#                         <div class="stat-item">
#                             <span>Avg Reel Plays: </span> {reelPlays}
#                         </div>

#                         <div class="stat-item">
#                             <span>Average View: </span> {avgViews}%
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
# template_html_file = 'rs-blog-template-new.html'  # Path to your updated HTML template file
# excel_file = 'RS-beauty-uae-new.xlsx'  # Path to your Excel file


# # Using f-string to create dynamic output file name
# niche_lower = 'beauty'  # You can extract this from your Excel or use as variable
# country_lower = 'uae'    # You can extract this from your Excel or use as variable
# output_html_file = f'best-{niche_lower}-influencers-in-{country_lower}.html'  # Dynamic output HTML file name

# generate_influencer_html(template_html_file, excel_file, output_html_file)




# ----------------------------------------------------------------------------------------


# rs latest template with new design


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

#        # Construct dynamic output file name based on niche and country extracted from Excel
#     # output_html_file = f'best-{niche_lower}-influencers-in-{country_lower}.html'

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
# template_html_file = 'realsubscriber-latest-template.html'  # Path to your updated HTML template file
# excel_file = 'RS-Lifestyle-uae-new.xlsx'  # Path to your Excel file


# # Using f-string to create dynamic output file name
# niche_lower = 'lifestyle'  # You can extract this from your Excel or use as variable
# country_lower = 'uae'    # You can extract this from your Excel or use as variable
# output_html_file = f'best-{niche_lower}-influencers-in-{country_lower}.html'  # Dynamic output HTML file name

# generate_influencer_html(template_html_file, excel_file, output_html_file)






# ------------------------------------------------------------------------------------
# RS with finding missing fields, 
# reel plays is commented
# 4 in line template




import pandas as pd
import random


# convert k and m into decimal
def convert_to_number(value):
    """Converts 'k' or 'M' formatted string to a number."""
    if isinstance(value, str):
        value = value.lower()  # Convert to lowercase to handle both 'K' and 'M'
        if value.endswith('k'):
            return float(value[:-1]) * 1_000
        elif value.endswith('m'):
            return float(value[:-1]) * 1_000_000
    return float(value)

# def calculate_gender_percentage(row):
#     """Calculates missing gender percentage dynamically based on provided input (either Male or Female)."""
#     if pd.notna(row['Female']) and row['Female'] != 'Unknown':
#         female_percentage = float(row['Female'].replace('%', '').strip())
#         male_percentage = 100 - female_percentage
#     elif pd.notna(row['Male']) and row['Male'] != 'Unknown':
#         male_percentage = float(row['Male'].replace('%', '').strip())
#         female_percentage = 100 - male_percentage
#     else:
#         female_percentage = 'Unknown'
#         male_percentage = 'Unknown'

#     return male_percentage, female_percentage


# calculate missing gender male or female both
def calculate_gender_percentage(row):
    """Calculates missing gender percentage dynamically based on provided input (either Male or Female)."""
    female_percentage = 'Unknown'
    male_percentage = 'Unknown'
    
    # Check if 'Female' column exists
    if 'Female' in row.index and pd.notna(row['Female']) and row['Female'] != 'Unknown':
        female_percentage = float(row['Female'].replace('%', '').strip())
        male_percentage = 100 - female_percentage
    # Check if 'Male' column exists
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

    # Iterate over the rows in the Excel sheet and generate the influencer content
    for index, row in data.iterrows():
        # Extract influencer details from the Excel file
        image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
        profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
        name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
        followers = row['Followers'] if pd.notna(row['Followers']) else '0'
        avgLikes = row['Average-Likes'] if pd.notna(row['Average-Likes']) else '0'
        # reelPlays = row['Reel-Plays'] if pd.notna(row['Reel-Plays']) else '0'

        # Convert followers, avgLikes, reelPlays to numeric values
        followers_num = convert_to_number(followers)
        avgLikes_num = convert_to_number(avgLikes)
        # reelPlays_num = convert_to_number(reelPlays)

        # Calculate missing fields
        if followers_num > 0:
            engagement_rate = (avgLikes_num / followers_num) * 100
            # avg_views = (reelPlays_num / followers_num) * 100
        else:
            engagement_rate = 0
            avg_views = 0

        # Calculate Male and Female percentages dynamically
        male_percentage, female_percentage = calculate_gender_percentage(row)

        # Dynamic rank generation (index starts at 0, so add 1 for ranking)
        rank = index + 1

        # Construct the HTML block for each influencer
        influencer_html = f"""
         <div class="influencer-profile">
            <div class="profile-header">
        <img class="profile-img" alt="{name}" src="{image}" />
        <div class="profile-info">
            <div class="blog-profile-wrapper">
                <h3 class="profile-name"><span class="profile-rank">{rank}.</span> <a href="{profileUrl}" target="_blank">{name}</a></h3>
                <p><i class="fa fa-instagram"></i><span>{followers}</span> Followers</p>
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

    # Replace placeholder in the HTML template with the generated influencer content
    final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)

    # Save the final HTML content into the output file
    with open(output_html_file, 'w', encoding='utf-8') as output_file:
        output_file.write(final_html_content)

    print(f"HTML file '{output_html_file}' generated successfully.")

# Example usage
template_html_file = 'realsubscriber-latest-template.html'  # Path to your updated HTML template file
excel_file = 'RS-home-decor.xlsx'  # Path to your Excel file

# Using f-string to create dynamic output file name
niche_lower = 'home-decor'  # You can extract this from your Excel or use as variable
country_lower = 'uae'    # You can extract this from your Excel or use as variable
output_html_file = f'best-{niche_lower}-influencers-in-{country_lower}.html'  # Dynamic output HTML file name

generate_influencer_html(template_html_file, excel_file, output_html_file)

