# Videase
# For 10 Listicle stratergy
# not countVar version because not in use in this code
# fully automate
# before use set the template because template include $countVar$ which is not in use in this script

import os
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
def generate_influencer_html(template_html_file, excel_file, output_folder):
    # Load the Excel file
    data = pd.read_excel(excel_file)

    # Fetch Niche and Country from the sheet
    niche = data.loc[0, 'Nichee'] if 'Nichee' in data.columns and pd.notna(data.loc[0, 'Nichee']) else 'Unknown Niche'
    country = data.loc[0, 'Country'] if 'Country' in data.columns and pd.notna(data.loc[0, 'Country']) else 'Unknown Country'

    # Prepare versions for file name
    niche_for_file = niche.lower().replace(" ", "-")  # Replace spaces with hyphens
    country_for_file = country.lower().replace(" ", "-")  # Replace spaces with hyphens

    # Preserve exact capitalization for placeholders
    niche_placeholder = niche  # Keep original capitalization from sheet
    country_placeholder = country  # Keep original capitalization from sheet

    total_influencers = len(data)

    # For not exceeding above 100 influencers
    max_influencers = 100
    if total_influencers > max_influencers:
        total_influencers = max_influencers

    # Rounding influencer count
    specified_values = {100, 90, 80, 70, 60, 50, 40, 30, 20, 10}
    if total_influencers not in specified_values:
        rounded_count = (total_influencers // 10) * 10
    else:
        rounded_count = total_influencers

    # Read the HTML template
    with open(template_html_file, 'r', encoding='utf-8') as file:
        html_template = file.read()
        
    # for small case
    niche_lower = niche.lower()

    # Replace placeholders with exact capitalization from sheet
    html_template = html_template.replace('$countVar$', str(rounded_count))
    html_template = html_template.replace('$NicheVar$', niche_placeholder)
    html_template = html_template.replace('$smallCase$', niche_lower.lower())
    html_template = html_template.replace('$CountryVar$', country_placeholder)
    html_template = html_template.replace('$NicheVarC$', niche_for_file)
    html_template = html_template.replace('$CountryVarC$', country_for_file)

    # List of words to randomize for PRandomVar
    random_words = ["follower count", "average reels plays", "average likes on their post", "male-female follower ratio"]
    prandom_var = ', '.join(random.sample(random_words, 4))
    html_template = html_template.replace('$PRandomVar$', prandom_var)

    placeholder_start = html_template.find('<div class="influencer-profile">')
    placeholder_end = html_template.find('<!-- Additional influencer profiles can go here -->')

    if placeholder_start != -1 and placeholder_end != -1:
        html_template = html_template[:placeholder_start] + html_template[placeholder_end:]

    # Placeholder for influencer list content
    influencer_content_list = ""

    # Select and process the required number of influencers sequentially
    selected_data = data.head(rounded_count)


    # Take the first 20 influencers, shuffle them, and then select 10
    first_20_influencers = data.head(20).sample(n=10, random_state=random.randint(1, 1000)).reset_index(drop=True)

    # Initialize rank counter
    rank = 1

    # for _, row in selected_data.iterrows():
    for _, row in first_20_influencers.iterrows():
  
        image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
        profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
        name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
        followers = row['Followers'] if pd.notna(row['Followers']) else '0'
        avgLikes = row['Average-Likes'] if pd.notna(row['Average-Likes']) else '0'
        reelPlays = row['Reel-Plays'] if pd.notna(row['Reel-Plays']) else '0'

        followers_num = convert_to_number(followers)
        avgLikes_num = convert_to_number(avgLikes)
        reelPlays_num = convert_to_number(reelPlays)

        # Calculate missing fields
        engagement_rate = (avgLikes_num / followers_num) * 100 if followers_num > 0 else 0
        avg_views = (reelPlays_num / followers_num) * 100 if followers_num > 0 else 0

        # Calculate Male and Female percentages dynamically
        male_percentage, female_percentage = calculate_gender_percentage(row)

        # Construct the HTML block for each influencer
        influencer_html = f"""
        <div class="influencer-profile">
            <div class="profile-header">
        <img class="profile-img" alt="{name}" src="{image}" />
        <div class="profile-info">
            <div class="blog-profile-wrapper">
                <h3 class="profile-name"><span class="profile-rank">{rank}.</span> <a href="{profileUrl}" rel="nofollow" target="_blank">{name}</a></h3>
                <p><i class="fab fa-instagram"></i><span>{followers}</span> Followers</p>
            </div>
              <div class="stats-block">
                     <div class="stats-wrapper">
                         <div class="stat-item">
                             <span>Engagement Rate: </span> {engagement_rate:.2f}%
                         </div>
                         <div class="stat-item">
                             <span>Avg Reel Plays: </span> {reelPlays}
                         </div>
                         <div class="stat-item">
                             <span class="stats-padd-right">Avg <br> Likes: </span> {avgLikes}
                         </div>
                     </div>

                     <div class="profile-stats-grid">
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

    # Replace placeholder in the HTML template with the generated influencer content
    final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)

    # Use niche and country to generate the output file name with hyphens
    output_html_file = os.path.join(output_folder, f'top-{niche_for_file}-instagrammers-in-{country_for_file}.html')

    # Save the final HTML content into the output file
    with open(output_html_file, 'w', encoding='utf-8') as output_file:
        output_file.write(final_html_content)

    print(f"HTML file '{output_html_file}' generated successfully.")

# Batch processing for all Excel files in a folder
def batch_process(template_html_file, folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            generate_influencer_html(template_html_file, file_path, output_folder)

# Example usage
template_html_file = './videase/videase5-template.html'  # Path to your updated HTML template file
folder_path = './AutoExcelSheets/'  # Folder containing Excel files
output_folder = './html_output/'  # Folder to save generated HTML files

batch_process(template_html_file, folder_path, output_folder)