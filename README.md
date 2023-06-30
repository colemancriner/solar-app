# Real-Time Solar
## Description
[Real-Time Solar](https://real-time-solar.streamlit.app/) is a web app I created for my college course midterm at the University of Maryland. More information can be found in the presentation tab of the web app [here](https://real-time-solar.streamlit.app/presentation). 

<sub>Note: The web app itself was my presentation. Bullet points may have little to no context for viewers.</sub>

### How it works
The web application is built using Streamlit, a powerful open-source Python library that seamlessly bridges Python and React for web development. By utilizing the srpenergy API client, users can securely log into their SRP Energy accounts and retrieve detailed hourly kWh and cost data. The data is then processed and organized into a clean and structured dataframe using the versatile pandas library. This includes essential data cleaning tasks such as resampling the data for different timeframes (hourly to daily, weekly, monthly, etc.) and converting data types. For instance, the date feature is converted to a datetime object using the datetime library. The final touch is given by creating visually appealing and interactive visualizations using various components provided by Streamlit.

## Course Context
### ARCH418C: Design Thinking, Innovations, and the future of Smart Green Buildings
### Description
This course explores the principles of design thinking, innovation, and the future of
sustainable architecture. Students will develop a holistic understanding of sustainable
design, circularity, modularity, system thinking, and smart infrastructure as it pertains to
the design of innovative buildings.
Through lectures, guest speaker sessions, case studies, and practical exercises,
students will gain the knowledge and skills necessary to design sustainable buildings
that are greener at a systemic level.
### Professor
Hooman Koliji is an accomplished architect and landscape designer whose expertise lies at the intersection of architecture and landscape. As a design researcher and clinical associate professor of architecture at the University of Maryland, he explores visual representation, spatial experience, and theories of imagination and design.
You can find more about Professor Koliji at the University of Maryland [School of Architecture website](https://arch.umd.edu/people/hooman-koliji) and his [LinkedIn](https://www.linkedin.com/in/koliji/).

