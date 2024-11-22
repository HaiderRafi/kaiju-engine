# import pandas as pd
# import random

# # Function to convert 'k' and 'M' values to numbers
# def convert_to_number(value):
#     """Converts 'k' or 'M' formatted string to a number."""
#     if isinstance(value, str):
#         value = value.lower().replace(',', '')  # Remove commas
#         if value.endswith('k'):
#             return float(value[:-1]) * 1_000
#         elif value.endswith('m'):
#             return float(value[:-1]) * 1_000_000
#     return float(value)

# # Calculate male and female percentages
# def calculate_gender_percentage(row):
#     """Calculates missing gender percentage dynamically based on provided input (either Male or Female)."""
#     female_percentage = 'Unknown'
#     male_percentage = 'Unknown'
    
#     if 'Female' in row.index and pd.notna(row['Female']) and row['Female'] != 'Unknown':
#         female_percentage = float(row['Female'].replace('%', '').strip())
#         male_percentage = 100 - female_percentage
#     elif 'Male' in row.index and pd.notna(row['Male']) and row['Male'] != 'Unknown':
#         male_percentage = float(row['Male'].replace('%', '').strip())
#         female_percentage = 100 - male_percentage

#     return male_percentage, female_percentage

# # Round down count unless it matches exact values
# def round_count_with_exceptions(total_influencers):
#     """Round down to nearest 10 unless the count is one of the specified values."""
#     exact_values = {100, 90, 80, 70, 60, 50, 40, 30, 20, 10}
    
#     if total_influencers in exact_values:
#         return total_influencers
#     return (total_influencers // 10) * 10

# def generate_influencer_html(template_html_file, excel_file, output_html_file):
#     # Load the Excel file
#     data = pd.read_excel(excel_file)

#     # Apply new rounding logic
#     total_influencers = len(data)
#     rounded_count = round_count_with_exceptions(total_influencers)

#     # Read the HTML template
#     with open(template_html_file, 'r', encoding='utf-8') as file:
#         html_template = file.read()

#     # Replace the $countVar$ placeholder with the rounded count
#     html_template = html_template.replace('$countVar$', str(rounded_count))

#     # Get the Niche and Country from the first row of the Excel file
#     niche = data.loc[0, 'Nichee'] if pd.notna(data.loc[0, 'Nichee']) else 'Unknown Niche'
#     country = data.loc[0, 'Country'] if pd.notna(data.loc[0, 'Country']) else 'Unknown Country'

#     # Prepare lowercase versions for Niche and Country
#     niche_lower = niche.lower()
#     country_lower = country.lower()

#     # Replace placeholders in the HTML template
#     html_template = html_template.replace('$NicheVar$', niche)
#     html_template = html_template.replace('$CountryVar$', country)
#     html_template = html_template.replace('$NicheVarC$', niche_lower)
#     html_template = html_template.replace('$CountryVarC$', country_lower)

#     # List of words to randomize for PRandomVar
#     random_words = ["average reel plays", "follower count", "male-to-female follower ratio", "average post likes"]

#     # Randomize words and replace $PRandomVar$
#     prandom_var = ', '.join(random.sample(random_words, 4))
#     html_template = html_template.replace('$PRandomVar$', prandom_var)

#     # Placeholder for influencer list content
#     influencer_content_list = ""

#     # Randomly select and process the required number of influencers
#     selected_data = data.head(rounded_count).sample(frac=1).reset_index(drop=True)
    
#     rank = 1
#     for _, row in selected_data.iterrows():
#         # Extract influencer details
#         image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
#         profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
#         name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
#         followers = row['Followers'] if pd.notna(row['Followers']) else '0'
#         avgLikes = row['Average-Likes'] if pd.notna(row['Average-Likes']) else '0'

#         # Convert to numeric values
#         followers_num = convert_to_number(followers)
#         avgLikes_num = convert_to_number(avgLikes)

#         # Calculate missing fields
#         engagement_rate = (avgLikes_num / followers_num) * 100 if followers_num > 0 else 0

#         # Calculate gender percentages
#         male_percentage, female_percentage = calculate_gender_percentage(row)

#         # Construct HTML block
#         influencer_html = f"""
#         <div class="influencer-profile">
#             <div class="profile-header">
#                 <img class="profile-img" alt="{name}" src="{image}" />
#                 <div class="profile-info">
#                     <div class="blog-profile-wrapper">
#                         <h3 class="profile-name"><span class="profile-rank">{rank}.</span> <a href="{profileUrl}" target="_blank" rel="nofollow">{name}</a></h3>
#                         <p><i class="fab fa-instagram"></i><span>{followers}</span> Followers</p>
#                     </div>
#                     <div class="stats-block">
#                         <div class="stats-wrapper">
#                             <div class="stat-item">
#                                 <span>Engagement Rate: </span> {engagement_rate:.2f}%
#                             </div>
#                             <div class="stat-item">
#                                 <span class="stats-padd-right">Avg <br> Likes: </span> {avgLikes}
#                             </div>
#                             <div class="stat-item">
#                                 <span>Male Audience: </span> {male_percentage if male_percentage == 'Unknown' else f'{male_percentage:.2f}'}%
#                             </div>
#                             <div class="stat-item">
#                                 <span>Female Audience: </span> {female_percentage if female_percentage == 'Unknown' else f'{female_percentage:.2f}'}%
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#         """
#         influencer_content_list += influencer_html
#         rank += 1

#     # Replace placeholder in the HTML template with generated content
#     final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)

#     # Save the final HTML content into the output file
#     with open(output_html_file, 'w', encoding='utf-8') as output_file:
#         output_file.write(final_html_content)

#     print(f"HTML file '{output_html_file}' generated successfully.")

# # Example usage
# template_html_file = 'grynowAuto.html'
# excel_file = 'testGrynowMoto.xlsx'

# niche_lower = 'test'
# country_lower = 'uae'
# output_html_file = f'top-{niche_lower}-influencers-in-{country_lower}.html'

# generate_influencer_html(template_html_file, excel_file, output_html_file)




# -------------------------------------------------------------

# working Fine
# but this is random list code with cropping the floor


import pandas as pd
import random

# Function to convert 'k' and 'M' values to numbers
def convert_to_number(value):
    """Converts 'k' or 'M' formatted string to a number."""
    if isinstance(value, str):
        value = value.lower().replace(',', '')  # Remove commas
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

    total_influencers = len(data)
    specified_values = {100, 90, 80, 70, 60, 50, 40, 30, 20, 10}

    if total_influencers not in specified_values:
        rounded_count = (total_influencers // 10) * 10
    else:
        rounded_count = total_influencers

        """Round down to nearest 10 unless the count is one of the specified values."""


    # Read the HTML template
    with open(template_html_file, 'r', encoding='utf-8') as file:
        html_template = file.read()

    # Replace the $countVar$ placeholder with the rounded count
    html_template = html_template.replace('$countVar$', str(rounded_count))

    # Get the Niche and Country from the first row of the Excel file
    niche = data.loc[0, 'Nichee'] if pd.notna(data.loc[0, 'Nichee']) else 'Unknown Niche'
    country = data.loc[0, 'Country'] if pd.notna(data.loc[0, 'Country']) else 'Unknown Country'

    # Prepare lowercase versions for Niche and Country
    niche_lower = niche.lower()
    country_lower = country.lower()

    # Replace placeholders in the HTML template
    html_template = html_template.replace('$NicheVar$', niche)
    html_template = html_template.replace('$CountryVar$', country)
    html_template = html_template.replace('$NicheVarC$', niche_lower)
    html_template = html_template.replace('$CountryVarC$', country_lower)

    # List of words to randomize for PRandomVar
    random_words = ["average reel plays", "follower count", "male-to-female follower ratio", "average post likes"]

    # Randomize words and replace $PRandomVar$
    prandom_var = ', '.join(random.sample(random_words, 4))
    html_template = html_template.replace('$PRandomVar$', prandom_var)

    # Remove the placeholder influencer block after populating
    placeholder_start = html_template.find('<div class="influencer-profile">')
    placeholder_end = html_template.find('<!-- Additional influencer profiles can go here -->')

    if placeholder_start != -1 and placeholder_end != -1:
        html_template = html_template[:placeholder_start] + html_template[placeholder_end:]

    # Placeholder for influencer list content
    influencer_content_list = ""

    # Randomly select and process the required number of influencers
    selected_data = data.head(rounded_count).sample(frac=1).reset_index(drop=True)
    
    rank = 1
    for _, row in selected_data.iterrows():
        # Extract influencer details
        image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
        profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
        name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
        followers = row['Followers'] if pd.notna(row['Followers']) else '0'
        avgLikes = row['Average-Likes'] if pd.notna(row['Average-Likes']) else '0'

        # Convert to numeric values
        followers_num = convert_to_number(followers)
        avgLikes_num = convert_to_number(avgLikes)

        # Calculate missing fields
        engagement_rate = (avgLikes_num / followers_num) * 100 if followers_num > 0 else 0

        # Calculate gender percentages
        male_percentage, female_percentage = calculate_gender_percentage(row)

        # Construct HTML block
        influencer_html = f"""
        <div class="influencer-profile">
            <div class="profile-header">
                <img class="profile-img" alt="{name}" src="{image}" />
                <div class="profile-info">
                    <div class="blog-profile-wrapper">
                        <h3 class="profile-name"><span class="profile-rank">{rank}.</span> <a href="{profileUrl}" target="_blank" rel="nofollow">{name}</a></h3>
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
        rank += 1

    # Replace placeholder in the HTML template with generated content
    final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)

    # Save the final HTML content into the output file
    with open(output_html_file, 'w', encoding='utf-8') as output_file:
        output_file.write(final_html_content)

    print(f"HTML file '{output_html_file}' generated successfully.")

# Example usage
template_html_file = 'grynowAuto.html'
excel_file = 'grynow-crypto-china.xlsx'

niche_lower = 'test'
country_lower = 'uae'
output_html_file = f'top-{niche_lower}-influencers-in-{country_lower}.html'

generate_influencer_html(template_html_file, excel_file, output_html_file)



# ----------------------------------------------------------------
# import pandas as pd
# import random

# # Convert 'k' and 'm' formatted string to number
# def convert_to_number(value):
#     """Converts 'k' or 'M' formatted string to a number."""
#     if isinstance(value, str):
#         value = value.lower()  # Handle both 'K' and 'M'
#         if value.endswith('k'):
#             return float(value[:-1]) * 1_000
#         elif value.endswith('m'):
#             return float(value[:-1]) * 1_000_000
#     return float(value)

# # Calculate missing gender percentages dynamically
# def calculate_gender_percentage(row):
#     """Calculates missing gender percentage dynamically based on provided input (either Male or Female)."""
#     female_percentage = 'Unknown'
#     male_percentage = 'Unknown'
    
#     if 'Female' in row.index and pd.notna(row['Female']) and row['Female'] != 'Unknown':
#         female_percentage = float(row['Female'].replace('%', '').strip())
#         male_percentage = 100 - female_percentage
#     elif 'Male' in row.index and pd.notna(row['Male']) and row['Male'] != 'Unknown':
#         male_percentage = float(row['Male'].replace('%', '').strip())
#         female_percentage = 100 - male_percentage

#     return male_percentage, female_percentage

# # Round down count unless it matches exact values
# def round_count_with_exceptions(total_influencers):
#     """Round down to nearest 10 unless the count is one of the specified values."""
#     exact_values = {100, 90, 80, 70, 60, 50, 40, 30, 20, 10}
    
#     if total_influencers in exact_values:
#         return total_influencers
#     return (total_influencers // 10) * 10

# def generate_influencer_html(template_html_file, excel_file, output_html_file):
#     # Load the Excel file
#     data = pd.read_excel(excel_file)

#     # Calculate total influencers and apply rounding
#     total_influencers = len(data)
#     rounded_count = round_count_with_exceptions(total_influencers)

#     # Read the HTML template
#     with open(template_html_file, 'r', encoding='utf-8') as file:
#         html_template = file.read()

#     # Get Niche and Country from the first row
#     niche = data.loc[0, 'Nichee'] if pd.notna(data.loc[0, 'Nichee']) else 'Unknown Niche'
#     country = data.loc[0, 'Country'] if pd.notna(data.loc[0, 'Country']) else 'Unknown Country'
#     niche_lower = niche.lower()
#     country_lower = country.lower()

#     # Replace placeholders in the HTML template
#     html_template = html_template.replace('$NicheVar$', niche)
#     html_template = html_template.replace('$CountryVar$', country)
#     html_template = html_template.replace('$NicheVarC$', niche_lower)
#     html_template = html_template.replace('$CountryVarC$', country_lower)
#     html_template = html_template.replace('$countVar$', str(rounded_count))

#     # Generate randomized PRandomVar content
#     random_words = ["follower count", "content quality", "engagement rate", "audience trust",
#                     "sentiment analysis", "brand collaborations"]
#     prandom_var = ', '.join(random.sample(random_words, 6))
#     html_template = html_template.replace('$PRandomVar$', prandom_var)

#     # Prepare influencer content
#     influencer_content_list = ""
#     for index, row in data.iterrows():
#         image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
#         profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
#         name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
#         followers = row['Followers'] if pd.notna(row['Followers']) else '0'
#         avgLikes = row['Average-Likes'] if pd.notna(row['Average-Likes']) else '0'
        
#         followers_num = convert_to_number(followers)
#         avgLikes_num = convert_to_number(avgLikes)
#         engagement_rate = (avgLikes_num / followers_num) * 100 if followers_num > 0 else 0
        
#         male_percentage, female_percentage = calculate_gender_percentage(row)
#         rank = index + 1

#         influencer_html = f"""
#         <div class="influencer-profile">
#             <div class="profile-header">
#                 <img class="profile-img" alt="{name}" src="{image}" />
#                 <div class="profile-info">
#                     <div class="blog-profile-wrapper">
#                         <h3 class="profile-name"><span class="profile-rank">{rank}.</span> <a href="{profileUrl}" target="_blank">{name}</a></h3>
#                         <p><i class="fa fa-instagram"></i><span>{followers}</span> Followers</p>
#                     </div>
#                     <div class="stats-block">
#                         <div class="stats-wrapper">
#                             <div class="stat-item">
#                                 <span>Engagement Rate: </span> {engagement_rate:.2f}%
#                             </div>
#                             <div class="stat-item">
#                                 <span class="stats-padd-right">Avg <br> Likes: </span> {avgLikes}
#                             </div>
#                             <div class="stat-item">
#                                 <span>Male Audience: </span> {male_percentage if male_percentage == 'Unknown' else f'{male_percentage:.2f}'}%
#                             </div>
#                             <div class="stat-item">
#                                 <span>Female Audience: </span> {female_percentage if female_percentage == 'Unknown' else f'{female_percentage:.2f}'}%
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#         """
#         influencer_content_list += influencer_html

#     final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)

#     with open(output_html_file, 'w', encoding='utf-8') as output_file:
#         output_file.write(final_html_content)

#     print(f"HTML file '{output_html_file}' generated successfully.")

# # Example usage
# # template_html_file = 'realsubscriber-latest-template.html'
# # excel_file = 'RS-home-decor.xlsx'
# # output_html_file = 'best-home-decor-influencers-in-uae.html'
# # generate_influencer_html(template_html_file, excel_file, output_html_file)

# template_html_file = 'grynowAuto.html'
# excel_file = 'testGrynowMoto.xlsx'

# niche_lower = 'test'
# country_lower = 'uae'
# output_html_file = f'top-{niche_lower}-influencers-in-{country_lower}.html'

# generate_influencer_html(template_html_file, excel_file, output_html_file)
