import streamlit as st

selected_slide = st.select_slider('Select a value', options=list(range(1, 11)), value=1)

if selected_slide == 1:
    st.title('Real-Time Solar')
    st.subheader('by Coleman Criner')

if selected_slide == 2:
    st.title('Problem Statement')
    st.subheader('How might we design a user-friendly software application or platform that effectively mitigates the barriers to purchase for homeowners, fostering the adoption of clean energy sources like solar?')

if selected_slide == 3:
    st.title('What Needs Fixing')
    st.subheader('Barriers to Purchase')
    st.markdown('- High upfront costs')
    st.markdown('- Lack of information')
    st.markdown('- Complex installation processes')
    st.markdown('- Limited access to financing options')

if selected_slide == 4:
    st.title('Research Insights')
    st.subheader('Key Findings from Interviews')
    st.markdown('- Homeowners')
    st.markdown('- Solar energy providers')
    st.markdown('- Renewable energy experts')

if selected_slide == 5:
    st.title('Changes to Improve the Experience')
    st.subheader('Designing a User-Friendly Software Application or Platform')
    st.markdown('- Provide transparent information about solar energy')
    st.markdown('- Streamline the purchasing process')
    st.markdown('- Offer financing options for homeowners')
    st.markdown('- Address concerns or misconceptions about solar power')

if selected_slide == 6:
    st.title('Idea 1: Solar Assessment and ROI Calculator')
    st.subheader('Key Features:')
    st.markdown('- Homeowners can input their location, energy consumption, and other data')
    st.markdown('- Generate a personalized solar assessment report')
    st.markdown('- Calculate return on investment (ROI)')
    st.markdown('- Consider factors like energy savings, incentives, and financing options')

    st.title('Idea 2: Virtual Solar Consultations')
    st.subheader('Key Features:')
    st.markdown('- Connect homeowners with solar energy experts for virtual consultations')
    st.markdown('- Schedule sessions to discuss needs, installation process, financing options')
    st.markdown('- Provide virtual site assessments, cost estimates, and recommendations')
    st.markdown('- Include a marketplace for comparing solar energy providers')

    
    
if selected_slide == 7:
    st.title('Pilot Version: Solar Assessment and ROI Calculator')
    st.subheader('Web-Based Application')
    st.markdown('- Intuitive steps for homeowners to input energy consumption and utility rates')
    st.markdown('- Algorithms generate a comprehensive solar assessment report')
    st.markdown('- Ideally, estimate cost savings, payback period, environmental impact')
    st.markdown('- Include information on available financing options')


if selected_slide == 8:
    st.title('Final Solution Design')
    st.subheader('User-Friendly Software Application for Solar Adoption')
    st.markdown('**Solution Description:**')
    st.markdown('- Clean and intuitive interface for easy navigation')
    st.markdown('- Comprehensive solar assessment and ROI calculation')
    st.markdown('- Personalized recommendations')
    st.markdown('- Integration with financing options and incentives')
    
    st.title('How the Solution Improves Sustainability and Experience')
    st.markdown('- Promotes clean energy adoption, reducing reliance on fossil fuels')
    st.markdown('- Lowers greenhouse gas emissions and carbon footprint')
    st.markdown('- Enables homeowners to make informed decisions about solar energy')
    st.markdown('- Streamlines the process, making it convenient and accessible')
    st.markdown('- Empowers homeowners to contribute to a sustainable future')

if selected_slide == 9:
    st.title('Project Reflections and Learnings')
    st.subheader('What We Learned:')
    st.markdown('- Importance of user-centered design approach')
    st.markdown('- Understanding barriers and concerns of homeowners')
    st.markdown('- Collaboration with solar energy experts and financial institutions')
    
    st.subheader('Surprises and Challenges:')
    st.markdown('- Complexity of integrating financing options')
    st.markdown('- Addressing varying regulations and incentives across regions')
    st.markdown('- Balancing simplicity with comprehensive information')
    
    st.subheader('What I Would Do Differently Next Time:')
    st.markdown('- Conduct more extensive user testing and iterations')
    st.markdown('- Explore partnerships with solar energy companies for real-world implementation')
    st.markdown('- Consider scalability and customization options for different markets')

if selected_slide == 10:
    st.title('Thank You!')
    st.subheader('Any Questions?')

