# For 10 Listicle stratergy
# not countVar version because not in use in this code
# for Borad Catogery in ugc
# SAME SAME



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
    random_words = ["audience trust", "quality of content", "engagement rate", "sentiment analysis", "brand collaborations"]

    # Randomly select words for PRandomVar and replace in template
    prandom_var = ', '.join(random.sample(random_words, 5))
    html_template = html_template.replace('$PRandomVar$', prandom_var)

    # Placeholder for influencer list content
    influencer_content_list = ""

    # Take the first 20 influencers, shuffle them, and then select 10
    first_20_influencers = data.head(20).sample(n=10, random_state=random.randint(1, 1000)).reset_index(drop=True)

    # Initialize rank counter
    rank = 1

    # Process influencers
    for _, row in first_20_influencers.iterrows():
        # Extract influencer details from the Excel file
        image = row['Image-URL'] if pd.notna(row['Image-URL']) else 'default_image.png'
        profileUrl = row['Profile-URL'] if pd.notna(row['Profile-URL']) else '#'
        name = row['Username'] if pd.notna(row['Username']) else 'Unknown'
        followers = row['Followers'] if pd.notna(row['Followers']) else '0'
        avgLikes = row['Average-Likes'] if pd.notna(row['Average-Likes']) else '0'
        reelPlays = row['Reel-Plays'] if pd.notna(row['Reel-Plays']) else '0'

        # Convert followers and avgLikes to numeric values
        followers_num = convert_to_number(followers)
        avgLikes_num = convert_to_number(avgLikes)
        reelPlays_num = convert_to_number(reelPlays)

        # Calculate engagement rate
        engagement_rate = (avgLikes_num / followers_num) * 100 if followers_num > 0 else 0
        avg_views = (reelPlays_num / followers_num) * 100

        # Calculate Male and Female percentages dynamically
        male_percentage, female_percentage = calculate_gender_percentage(row)

        # Construct the HTML block for each influencer with correct rank
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
        rank += 1  # Increment the rank for the next influencer

    # Remove the placeholder block
    placeholder_start = html_template.find('<div class="influencer-profile">')
    placeholder_end = html_template.find('<!-- Additional influencer profiles can go here -->')

    if placeholder_start != -1 and placeholder_end != -1:
        html_template = html_template[:placeholder_start] + html_template[placeholder_end:]

    # Replace placeholder in the HTML template with the generated influencer content
    final_html_content = html_template.replace("<!-- Additional influencer profiles can go here -->", influencer_content_list)

    # Save the final HTML content into the output file
    with open(output_html_file, 'w', encoding='utf-8') as output_file:
        output_file.write(final_html_content)

    print(f"HTML file '{output_html_file}' generated successfully.")

# Example usage
template_html_file = './igy/broadUgc/igy5-template-broad.html'  # Path to your updated HTML template file
excel_file = './rs-ytInsta-igPackages-ugc-usa.xlsx'  # Path to your Excel file

# niche_lower = 'arab'  # You can extract this from your Excel or use as variable
country_lower = 'usa'    # You can extract this from your Excel or use as variable
output_html_file = f'best-ugc-content-creators-on-instagram-in-{country_lower}.html'  # Dynamic output HTML file name

generate_influencer_html(template_html_file, excel_file, output_html_file)
