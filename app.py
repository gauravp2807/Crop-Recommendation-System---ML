import numpy as np
import pandas as pd
import streamlit as st
import pickle

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)


st.set_page_config(page_title='None', page_icon='🌱', layout="centered", initial_sidebar_state="auto", menu_items={'About':"This is me - https://www.linkedin.com/in/gaurav-prajapati-170933211/"})

st.markdown("""
    <style>
    body {
        background-color: #f0fff0;  /* Light green / honeydew */
    }
    </style>
    """, unsafe_allow_html=True)



def intro():
    import streamlit
    st.sidebar.success("select what you want to know.")
    st.markdown(
        """
        ## Welcome to our Farmer's Corner! by Gaurav
    """
    )

    st.caption(
    '''
    Discover the perfect crops for your land by simply inputting your farm's specifications.
    Our smart tool will provide tailored recommendations, ensuring your agricultural success. 
    ''')

    st.caption('''
    Explore our curated crop insights for expert tips on cultivation, challenges, and market
    trends. Maximize your farm's potential with us!''')


def crop_recommend():
    import numpy as np
    import pandas as pd
    import streamlit as st
    import pickle

    encoder=pickle.load(open('encoder.pkl','rb'))
    rfc=pickle.load(open('rfc.pkl','rb'))

    st.write('''
    ## Most Suitable Crop for your farm 🌾
    '''

    )

    st.write("Now Tell me something about your farm")


    def user_input_para():
        n=st.number_input('Nitrogen (kg/hect)',min_value=0.0,step=None)
        p=st.number_input('Phosphorus (kg/hect)',min_value=0.0)
        k=st.number_input('Potassium (kg/hect)',min_value=0.0)
        t=st.number_input('temperature (°C)',min_value=0.0)
        h=st.number_input('humidity (%)',min_value=0.0,max_value=100.00)
        ph=st.number_input('ph',min_value=0.0,max_value=14.00)
        rain=st.number_input('rainfall (mm)',min_value=0.0)
        data={'N':n,'P':p,'K':k,'temperature':t,'humidity':h,'ph':ph,'rainfall':rain}
        features=pd.DataFrame(data,index=[0])
        return features

    input_data=user_input_para()
    st.subheader('So these are specifications of your farm 🚜')
    st.write(input_data)

    prediction=rfc.predict(input_data)
    if st.button('Predict'):
        if (input_data!=0).all().all():
            st.subheader('You should Grow 🌿')
            st.caption(encoder.inverse_transform(prediction)[0])
        else:
            st.caption('please give input')

def know_crop():
    import streamlit as st
    import time
    import numpy as np
    st.write('''
        ## Welcome Kisan 🌾
        ''')
    st.markdown(
        """
        #### Which crop would you like to know about?
    """
    )
    crop_name= st.selectbox(
        'Select the crop name',
        ('','Bajra', 'Barley','Cotton','Guar','Gram/Chana','Groundnut','Maize','Millet','Rice','Sorghum','Soybean','Wheat',))

    if crop_name=='Bajra':
        st.image('https://gonefarmers.com/cdn/shop/products/image_26dd2d63-7030-4712-994e-4ba84c8ca662_1024x1024@2x.jpg?v=1669047407',caption='Bajra',width=600)
        st.caption('''
        Bajra grows very well in dry and warm climatic regions, and it is a drought–
        tolerant crop that quite low annual rainfall of 40 cm to 60 cm. The ideal tempe
        -rature range for Bajra cultivation is 20°C to 30°C. During its vegetative growth,
        moist weather is beneficial. Bajra is grown as a Kharif crop in North India and as
        a summer crop in some southern areas that receive irrigation. Bajra is also grown 
        as winter crop in some regions within India.''')
        st.subheader('Season')
        st.caption('''
        Bajra is a warm-season crop that is typically sown during the summer, rainy season
        The sowing time varies depending on the region, but it generally occurs from May to
        July in India''')
        st.subheader('Water and Other Nutrient Requirements')
        st.caption('''
        Bajra is relatively drought-tolerant compared to other cereal crops, but it still
        requires adequate water for proper growth and development. The crop performs well
        in well-drained soils. While it requires less water than other crops, a timely and
        appropriate water supply is essential during critical growth stages.
        As for nutrient requirements, bajra benefits from balanced fertilization. Nitrogen,
        phosphorus, and potassium are essential nutrients for its growth. Proper soil
        testing and nutrient management are crucial to achieve optimal yields.''')
        st.subheader('Price Range')
        st.caption('''
        The price of bajra can vary based on factors such as demand, supply, market con
        -ditions and quality. Bajra is often traded as a commodity, and its prices can
        fluctuate based on local and global factors.
        As per the latest market rates, the average Bajra(Pearl Millet/Cumbu) price is 
        ₹2140.88/Quintal. The lowest market price is ₹1360/Quintal.''')
        st.subheader('Top Bajra Producing States in India')
        st.caption('''
        The top bajra-producing states in India include Rajasthan, Gujarat, Maharashtra
        Uttar Pradesh, and Haryana.''')
        st.subheader('Machinery Requirements')
        st.caption('''
        Common agricultural machinery used for bajra cultivation includes ploughs ,
        harrows, seed drills, tractors, threshers, and combine harvesters. The choice
        of machinery depends on the scale of cultivation and the farming practices in
        the region.''')
        st.subheader('Fertilizers and Farming Techniques')
        st.caption('''
        Bajra cultivation requires proper fertilization to achieve good yields. Common
        fertilizers used include urea, diammonium phosphate (DAP), and muriate of 
        potash (MOP). Organic manures can also be beneficial for soil health and 
        nutrient retention. 
        Farming techniques for bajra involve proper land preparation, timely sowing,
        spacing, and weed management. Bajra is often grown as a rain-fed crop, but
        irrigation can be used during dry spells.''')
        st.subheader('Bajra Crop Diseases')
        st.caption('''
        Common diseases affecting bajra include downy mildew, ergot, smut, and rust.
        Proper crop rotation, use of disease-resistant varieties, and timely appli-
        cation of appropriate fungicides are important disease management practices.''')
        st.subheader('Bajra as a Food')
        st.caption('''
        Bajra is consumed in various forms, including as whole grains, flour, porridge,
        and traditional dishes. It is often used to make flatbreads (roti) and is a 
        staple in many Indian households.''')
        st.subheader('Bajra Nutritional Information')
        st.caption('''
        Bajra is rich in dietary fiber, essential minerals like iron and magnesium, and
        B-vitamins. It is gluten-free and has a lower glycemic index compared to wheat,
        making it a nutritious option for those with dietary restrictions and for 
        managing blood sugar levels.''')

    if crop_name == 'Barley':
        st.image('https://cdn.britannica.com/31/75931-050-FED41F1F/Barley.jpg',caption='Barley')
        st.caption('''
        Barley (Hordeum vulgare) is a versatile cereal crop known for its adaptability to
        various climatic conditions. It is cultivated for both human consumption and 
        livestock feed. Barley has a relatively short growth cycle compared to other 
        cereal crops, making it a popular choice in regions with shorter growing seasons.''')

        st.subheader('Season')
        st.caption('''
        Barley is typically grown as a winter season crop in India, sown during the 
        Rabi season.
        Sowing usually takes place from October to November, and harvesting occurs 
        in March to April. This choice of season is due to barley's ability to withstand
        colder temperatures during its growth period.''')

        st.subheader('Water and Other Nutrient Requirements')
        st.caption('''
        Barley has moderate water requirements and can tolerate drier conditions than 
        some other cereal crops. However, adequate water is still necessary for proper
        growth and grain development. Balanced nutrient management is essential for 
        barley cultivation. Nitrogen, phosphorus, and potassium are the primary nutrients
        required. Soil testing guides the application of fertilizers to ensure optimal
        yields.''')

        st.subheader('Price Range')
        st.caption('''
        The price of barley can vary based on factors such as demand, quality, and 
        market conditions. As of my last knowledge update, the price range for barley
        in India could vary from around Rs. 1,200 to Rs. 1,800 per quintal (100 kilograms).
        These prices can fluctuate based on local and global market dynamics.''')

        st.subheader('Top Barley Producing States in India')
        st.caption('''
        The top barley-producing states in India include Rajasthan, Uttar Pradesh,
        Madhya Pradesh, Haryana, and Punjab. These states have favorable climatic
        conditions for successful barley cultivation.''')

        st.subheader('Machinery Requirements')
        st.caption('''
        Common agricultural machinery used for barley cultivation includes ploughs,
        seed drills,tractors, combine harvesters, and threshers. The choice of 
        machinery depends on the scale of cultivation and the specific farming 
        practices in the region.''')

        st.subheader('Fertilizers and Farming Techniques')
        st.caption('''
        Barley cultivation requires proper fertilization to achieve optimum yields.
        Common fertilizers like urea, diammonium phosphate (DAP), and muriate of 
        potash (MOP) are used. Precision in fertilizer application, along with 
        appropriate tillage practices and timely sowing, contributes to successful
        barley farming.''')

        st.subheader('Barley Crop Diseases')
        st.caption('''
        Barley is susceptible to various diseases such as rust, smut, powdery mildew,
        and net blotch. Integrated disease management strategies, including the use 
        of disease-resistant varieties and timely application of fungicides, are 
        crucial to mitigate disease impacts.''')

        st.subheader('Barley as Food')
        st.caption('''
        Barley is consumed as a whole grain and is used to make various food products,
        including barley flour, pearl barley, and barley grits. It is used in soups, 
        stews, salads, and as an ingredient in bread and bakery products.''')

        st.subheader('Barley Nutritional Information')
        st.caption('''
        Barley is a nutritious cereal, rich in dietary fiber, vitamins (B-complex), and
        minerals (magnesium, phosphorus, and selenium). It has a lower glycemic index 
        compared to some other grains, making it a favorable choice for managing blood 
        sugar levels and promoting satiety.''')


    if crop_name == 'Cotton':
        st.image('https://www.worldatlas.com/r/w1200/upload/c4/14/a0/shutterstock-738008380.jpg',caption='Cotton/Narma',width=600)
        st.caption('''
        Cotton (Gossypium hirsutum) is a significant cash crop known for its versatile
        use in the textile industry. It is valued for its natural fibers, which are spun
        into yarn and used to produce clothing, fabrics, and more.''')

        st.subheader('Season')
        st.caption('''
        Cotton is primarily a Kharif crop, meaning it is sown during the monsoon season
        in India. The sowing period typically starts from June and continues until August.
        The crop requires warm temperatures and ample sunlight for proper growth and fiber
        development.''')

        st.subheader('Water and Other Nutrient Requirements')
        st.caption('''
        Cotton has moderate water requirements during its growing period. Adequate 
        irrigation is crucial for the development of healthy cotton bolls. Nutrient
        requirements include nitrogen, phosphorus, and potassium, along with micronutrients
        Proper soil testing and balanced nutrient management are essential for high cotton 
        yields.''')

        st.subheader('Price Range')
        st.caption('''
        The price of cotton can vary significantly due to global demand and supply factors
        , quality, and market conditions. As of my last knowledge update, the price range
        for raw cotton in India could vary from around Rs. 5,000 to Rs. 6,500 per quintal
        (100 kilograms). These prices can experience fluctuations due to various economic
        and market factors.''')

        st.subheader('Top Cotton Producing States in India')
        st.caption('''
        The top cotton-producing states in India include Gujarat, Maharashtra, Telangana,
        Andhra Pradesh, and Punjab. These states have favorable climatic conditions and 
        suitable agricultural practices for successful cotton cultivation.''')

        st.subheader('Machinery Requirements')
        st.caption('''
        Cotton cultivation involves various machinery and equipment, including tractors,
        cultivators, planters, sprayers, and cotton pickers. Modern cotton farming often
        utilizes machinery for planting, irrigation, weed control, and harvesting to 
        increase efficiency and yields.''')

        st.subheader('Fertilizers and Farming Techniques')
        st.caption('''
        Cotton farming requires fertilization to support healthy growth and boll 
        development. Common fertilizers such as urea, DAP (diammonium phosphate), and MOP
        (muriate of potash) are used. Integrated pest management techniques, proper
        irrigation management, and weed control practices are also crucial for successful 
        cotton cultivation.''')

        st.subheader('Cotton Crop Diseases')
        st.caption('''
        Cotton is susceptible to various diseases, including cotton wilt, bollworm 
        infestation and bacterial blight. Disease management strategies include using
        disease-resistant cotton varieties, practicing crop rotation, and implementing
        proper sanitation and pest control measures.''')

        st.subheader('Cotton Uses')
        st.caption('''
        Cotton is widely used in the textile industry for producing clothing, fabrics
        home textiles, and industrial products. Apart from textiles, cottonseed oil 
        is extracted from cottonseeds and is used for cooking and as an ingredient in
        various food products. Cottonseed meal is also used as animal feed.''')

    if crop_name == 'Guar':
        st.image('https://i.ytimg.com/vi/T5Sc2qj7RqQ/maxresdefault.jpg',caption='Guar',width=600)
        st.caption('''
        Guar (Cyamopsis tetragonoloba), commonly known as gwar or guar gum, is an 
        important leguminous crop cultivated for its seeds and gum. Guar gum is used in
        various industries, including food, pharmaceuticals and textiles.''')

        st.subheader('Season')
        st.caption('''
        Guar is predominantly grown as a Kharif crop, sown during the monsoon season
        in India. The ideal sowing time is from June to July. Guar plants thrive in 
        warm temperatures and are well-suited for regions with longer daylight hours.''')

        st.subheader('Water and Other Nutrient Requirements')
        st.caption('''
        Guar is known for its ability to withstand drought conditions due to its
        deep root system. It requires less water than many other crops. Adequate soil
        moisture during critical growth stages is essential. The crop has nitrogen-
        fixing capabilities, reducing its external nitrogen requirement. However, it
        benefits from phosphorus and potassium supplementation.''')

        st.subheader('Price Range')
        st.caption('''
        The price of guar gum can fluctuate based on global demand, supply, quality,
        and market conditions. As of my last knowledge update, the price range for 
        guar gum could vary from around Rs. 5,000 to Rs. 8,000 per quintal or even 
        higher. These prices are influenced by various economic and market factors.''')

        st.subheader('Top Gwar Producing States in India')
        st.caption('''
        The top guar-producing states in India include Rajasthan, Gujarat, Haryana, 
        and Punjab. These states have favorable climatic conditions for successful
        guar cultivation.''')

        st.subheader('Machinery Requirements')
        st.caption('''
        Common agricultural machinery used for guar cultivation includes ploughs,
        cultivators, seed drills,tractors, and threshers. Mechanized equipment is used
        for planting, irrigation, and harvesting to enhance efficiency.''')

        st.subheader('Fertilizers and Farming Techniques')
        st.caption('''
        Guar cultivation generally requires less external fertilization due to its
        nitrogen-fixing ability. However, phosphorus and potassium application is 
        important. Proper spacing, weed management, and irrigation practices 
        contribute to healthy guar plants.''')

        st.subheader('Gwar Crop Diseases')
        st.caption('''
        Guar is relatively resilient to diseases, but it can still be affected by
        root rot, wilt, and fungal
        infections. Practicing good field hygiene, crop rotation, and choosing 
        disease-resistant varieties help manage potential issues.''')

        st.subheader('Gwar as Food')
        st.caption('''
        Guar seeds are used as a food source, mainly in the form of guar gum, which
        is derived from the endosperm of the seeds. Guar gum is a common food additive
        used as a thickener, stabilizer, and emulsifier in various processed foods.''')

        st.subheader('Gwar Uses')
        st.caption('''
        Apart from its applications in the food industry, guar gum is widely used in
        the oil and gas sector, textile industry, pharmaceuticals, cosmetics, and 
        more. It is utilized as a stabilizer in hydraulic fracturing (fracking) fluids,
        as a binder in tablets, and as a sizing agent in textiles.''')

    if crop_name == 'Gram/Chana':
        st.image('https://c1.wallpaperflare.com/preview/157/884/882/chickpea-india-grain-vegetarian.jpg',caption='Gram/Chana',width=600)
        st.caption('''
        Gram (Cicer arietinum), commonly known as chickpea or Chana, is a widely 
        cultivated pulse crop known for its nutritional value and versatility in 
        culinary applications.''')

        st.subheader('Season')
        st.caption('''
        Gram is typically grown as a Rabi crop in India, sown during the winter season.
        The ideal sowing time is from October to December. It benefits from cooler 
        temperatures during its growth period.''')

        st.subheader('Water and Other Nutrient Requirements')
        st.caption('''
        Gram has moderate water requirements and can tolerate drier conditions than some
        other crops. Adequate soil moisture during flowering and pod development stages is
        essential for higher yields. Gram requires nitrogen,phosphorus, and potassium 
        fertilization for optimal growth and production.''')

        st.subheader('Price Range')
        st.caption('''
        The price of gram can vary based on factors such as demand, supply, 
        quality, and market conditions. As of my last knowledge update, the price
        range for gram in India could vary from around Rs. 4,000 to Rs. 5,500 per
        quintal (100 kilograms). These prices can fluctuate due to economic and 
        market dynamics.''')

        st.subheader('Top Gram Producing States in India')
        st.caption('''
        The top gram-producing states in India include Madhya Pradesh, Rajasthan, 
        Maharashtra, Uttar Pradesh, and Andhra Pradesh. These states have 
        favorable agro-climatic conditions for successful gram cultivation.''')

        st.subheader('Machinery Requirements')
        st.caption('''
        Common agricultural machinery used for gram cultivation includes ploughs,
        cultivators, seed drills, tractors, and threshers. Mechanized equipment
        assists in land preparation, sowing, and harvesting.''')

        st.subheader('Fertilizers and Farming Techniques')
        st.caption('''
        Gram cultivation requires proper fertilization to achieve optimum yields.
        Common fertilizers such as urea, DAP (diammonium phosphate), and MOP 
        (muriate of potash) are used. Balanced nutrient management and proper
        spacing contribute to successful gram farming.''')

        st.subheader('Gram Crop Diseases')
        st.caption('''
        Gram can be affected by diseases such as wilt, blight, and root rot. 
        Disease management involves using disease-resistant varieties, practicing crop 
        rotation, and applying appropriate fungicides when necessary.''')

        st.subheader('Gram as Food')
        st.caption('''
        Gram is consumed in various forms, including boiled as a snack, ground into flour
        (besan) for making snacks, sweets, and other dishes, and used as an ingredient 
        in curries and soups.''')

        st.subheader('Gram Uses')
        st.caption('''
        Apart from being a staple food in many cuisines, gram is used for making besan
        (gram flour), which is widely used in culinary applications. It is also used in 
        traditional dishes, snacks, and as an ingredient in various processed foods.''')

    if crop_name == 'Groundnut':
        st.image('https://media.istockphoto.com/id/616003590/photo/peanuts.jpg?b=1&s=612x612&w=0&k=20&c=vTlkScITOXukZJ1zcH2KMDEC9WvzhjciGtLmGqoSd44=',caption='Groundnut',width=600)
        st.caption('''
        Groundnut (Arachis hypogaea), commonly known as peanut or shengdana, is an 
        important oilseed crop cultivated for its seeds, which are rich in oil and 
        protein.''')

        st.subheader('Season')
        st.caption('''
        Groundnut is grown as a Kharif and Rabi crop in India, making it a versatile crop
        with varying sowing times across different regions. The Kharif season sowing occurs
        from June to August, while the Rabi season sowing is from November to December.''')

        st.subheader('Water and Other Nutrient Requirements')
        st.caption('''
        Groundnut requires a consistent water supply for proper pod development. It is  
        sensitive to water stress during flowering and pegging stages. Adequate nitrogen,
        phosphorus, and potassium are important for higher yields. Groundnut is also known
        for its ability to fix atmospheric nitrogen.''')

        st.subheader('Price Range')
        st.caption('''
        The price of groundnut can vary based on factors such as demand, supply, quality,
        and market conditions.As of my last knowledge update, the price range for groundnut
        in India could vary from around Rs. 4,000 to Rs. 6,000 per quintal (100 kilograms).
        Prices can be influenced by various economic and market factors.''')

        st.subheader('Top Groundnut Producing States in India')
        st.caption('''
        The top groundnut-producing states in India include Gujarat, Andhra Pradesh,
        Tamil Nadu, Karnataka, and Rajasthan. These states have favorable agro-climatic 
        conditions for successful groundnut cultivation.''')

        st.subheader('Machinery Requirements')
        st.caption('''
        Common agricultural machinery used for groundnut cultivation includes ploughs,
        seed drills, tractors, cultivators, and harvesters. Mechanized equipment helps
        in planting, intercultural operations, and harvesting of groundnut.''')

        st.subheader('Fertilizers and Farming Techniques')
        st.caption('''
        Groundnut cultivation requires nitrogen, phosphorus, and potassium 
        fertilization for optimal growth. Balanced nutrient management, proper spacing,
        and weed management contribute to successful groundnut farming. Intercropping
        with leguminous crops can enhance soil fertility and nitrogen fixation.''')

        st.subheader('Groundnut Crop Diseases')
        st.caption('''
        Common diseases affecting groundnut include rust, early and late leaf spot, 
        and aflatoxin contamination. Use of disease-resistant varieties, crop rotation,
        and timely application of appropriate fungicides are important for disease 
        management.''')

        st.subheader('Groundnut as Food')
        st.caption('''
        Groundnuts are consumed in various forms, including roasted, boiled, and used
        as ingredients in various cuisines. Groundnut oil is extracted from the seeds
        and is used for cooking and in the food industry.''')

        st.subheader('Groundnut Uses')
        st.caption('''
        Apart from being a popular snack and cooking oil source, groundnuts are used 
        to make peanut butter, groundnut oil, and various processed foods. Groundnut 
        cake, a byproduct of oil extraction, is used as animal feed and organic 
        fertilizer.''')

    if crop_name == 'Maize':
        st.image('https://images.unsplash.com/photo-1634467524884-897d0af5e104?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y29ybnxlbnwwfHwwfHx8MA%3D%3D&w=1000&q=80',caption='Maize',width=600)
        st.caption('''
        Maize (Zea mays), commonly known as corn, is a cereal grain that is widely 
        cultivated for its versatile uses in food, fodder, and industrial applications.''')

        st.subheader('Season')
        st.caption('''
        Maize is typically grown during the Kharif season in India, which corresponds 
        to the monsoon period from June to September. The exact sowing time may vary
        depending on the region and local climate.''')

        st.subheader('Water and Other Nutrient Requirements')
        st.caption('''
        Maize requires a sufficient amount of water during its growing period, 
        especially during critical stages such as flowering and grain filling. Adequate
        moisture is important for optimal yield. Nitrogen, phosphorus, and potassium 
        are essential nutrients for maize cultivation. Nitrogen is particularly 
        crucial for healthy plant growth and grain development.''')

        st.subheader('Price Range')
        st.caption('''
        The price of maize can vary based on factors such as demand, supply, quality,
        and market conditions. Maize is used for various purposes, including food, 
        animal feed, and industrial processing. Prices can fluctuate based on these
        different uses and market dynamics.''')

        st.subheader('Top Maize Producing States in India')
        st.caption('''
        The top maize-producing states in India include Karnataka, Andhra Pradesh,
        Telangana, Madhya Pradesh, Maharashtra,Uttar Pradesh, and Bihar. These states
        have suitable agro-climatic conditions for maize cultivation.''')

        st.subheader('Machinery Requirements')
        st.caption('''
        Common agricultural machinery used for maize cultivation includes ploughs, 
        harrows, seed drills, planters, tractors, and combine harvesters. Mechanized
        equipment helps in various stages of maize farming, from planting to harvesting.''')

        st.subheader('Fertilizers and Farming Techniques')
        st.caption('''
        Maize cultivation requires balanced nutrient management. Nitrogen is particularly
        important for good yield and grain quality. Proper spacing, timely sowing, weed
        and pest management, and soil fertility maintenance are crucial for successful 
        maize farming.''')

        st.subheader('Maize Crop Diseases')
        st.caption('''
        Common diseases affecting maize include stalk rots, leaf blights, and downy 
        mildew. Disease management involves using disease-resistant varieties, crop 
        rotation, and applying appropriate fungicides and cultural practices.''')

        st.subheader('Maize as Food')
        st.caption('''
        Maize is consumed in various forms, including as fresh corn, popcorn, cornmeal,
        cornflour, and various processed foods. It is a staple food in many cultures and
        is used in a wide range of dishes.''')

        st.subheader('Maize Uses')
        st.caption('''
        Apart from its use as a food source, maize is used for animal feed, in industrial
        applications for producing corn starch, corn syrup, and ethanol, and as a raw 
        material for various food and non-food products such as oils, cereals, and snacks.''')

    if crop_name == 'Millet':
        st.image(
            'https://media.istockphoto.com/id/458218433/photo/varieties-of-grains-seeds-and-beans.jpg?s=612x612&w=0&k=20&c=WoWQn212OY15nbdZGkAVBKgW6AxOHlg_zgH6pBzDlzE=',
            caption='Millet', width=600)

        st.caption('''
        Millet is a group of small-seeded grasses that are cultivated for their edible 
        seeds. They are hardy and versatile crops that can thrive in diverse agro-climatic
        conditions.''')

        st.subheader('Season')
        st.caption('''
        Millet crops are typically grown during the Kharif season in India, which 
        corresponds to the monsoon period from June to September. The specific sowing time
        varies depending on the type of millet and the region.''')

        st.subheader('Water and Other Nutrient Requirements')
        st.caption('''
        Millet is known for its drought-resistant nature and can tolerate lower water 
        availability compared to other cereal crops. It is suitable for regions with low
        rainfall. Millet crops have relatively modest nutrient requirements, with a focus
        on nitrogen, phosphorus, and potassium for optimal growth and yield.''')

        st.subheader('Price Range')
        st.caption('''
        The price of millet can vary based on factors such as the type of millet, demand
        supply, market conditions, and quality. Different types of millet are used for 
        various purposes, including food, fodder, and industrial uses.''')

        st.subheader('Top Millet Producing States in India')
        st.caption('''
        The top millet-producing states in India include Rajasthan, Andhra Pradesh, 
        Karnataka, Tamil Nadu, Maharashtra, and Telangana. These states have favorable 
        agro-climatic conditions for millet cultivation.''')

        st.subheader('Machinery Requirements')
        st.caption('''
        Common agricultural machinery used for millet cultivation includes ploughs, seed
        drills, harrows, tractors, threshers, and other equipment for planting and 
        harvesting. The choice of machinery depends on the type of millet and the local
        farming practices.''')

        st.subheader('Fertilizers and Farming Techniques')
        st.caption('''
        Millet cultivation requires appropriate soil preparation, timely sowing, and weed
        management. Depending on the soil conditions, millets may require the application
        of organic manures and balanced fertilization with nitrogen, phosphorus, and 
        potassium.''')

        st.subheader('Millet Crop Diseases')
        st.caption('''
        Common diseases affecting millet crops include smut, rust, and downy mildew. 
        Disease management involves the use of disease-resistant varieties, proper crop
        rotation, and the application of suitable fungicides.''')

        st.subheader('Millet as Food')
        st.caption('''
        Millet is used as a staple food in various cultures and cuisines. It is consumed
        in different forms, including whole grains, flour, porridge, and traditional 
        dishes. Millet is known for its nutritional value and gluten-free nature.''')

        st.subheader('Millet Uses')
        st.caption('''
        Apart from its use as a food source, millet is used for animal fodder, in the 
        production of alcoholic beverages (as in sorghum-based traditional drinks),
        and for industrial applications such as biofuels and manufacturing various
        products like paper and building materials.''')


    if crop_name == 'Rice':
        st.image(
            'https://img.freepik.com/free-photo/top-view-delicious-boiled-rice-with-raw-rice-inside-little-plate-dark-desk_179666-27203.jpg',
            caption='Rice', width=600)
        st.caption('''
        Rice is a staple food crop that is widely consumed around the world. It is a
        major source of calories and nutrition for billions of people.''')

        st.subheader('Season')
        st.caption('''
        Rice is typically grown in two main seasons: Kharif (monsoon) and Rabi (winter).
        In India, Kharif rice is sown during the monsoon season, from June to July, and
        harvested from October to December. Rabi rice is sown during the winter season, 
        from November to December, and harvested from April to May.''')

        st.subheader('Water and Other Nutrient Requirements')
        st.caption('''
        Rice is a water-intensive crop and requires a consistent supply of water for 
        proper growth. It can be grown in both irrigated and rainfed conditions. 
        Nutrient requirements for rice include nitrogen, phosphorus, and potassium. Proper
        soil testing and nutrient management are essential for optimal yield.''')

        st.subheader('Price Range')
        st.caption('''
        The price of rice can vary based on factors such as the variety of rice, demand
        , supply, market conditions, and quality. Rice is traded globally, and its prices
         can be influenced by international markets.''')

        st.subheader('Top Rice Producing States in India')
        st.caption('''
        The top rice-producing states in India include West Bengal, Uttar Pradesh, Punjab
        , Andhra Pradesh, Telangana, and Bihar. These states have favorable agro-climatic
        conditions for rice cultivation.''')

        st.subheader('Machinery Requirements')
        st.caption('''
        Common agricultural machinery used for rice cultivation includes ploughs, seed
        drills, tractors, transplanters, threshers, and other equipment for planting, 
        transplanting, and harvesting. The choice of machinery depends on the scale of 
        cultivation and the farming practices.''')

        st.subheader('Fertilizers and Farming Techniques')
        st.caption('''
        Rice cultivation involves different techniques such as direct seeding and 
        transplanting. Fertilization includes the application of nitrogen, phosphorus, and
        potassium. Rice fields may require water management techniques, such as puddling
        and levee systems.''')

        st.subheader('Rice Crop Diseases')
        st.caption('''
        Common diseases affecting rice include blast, bacterial leaf blight, and sheath 
        blight. Disease management includes the use of disease-resistant varieties, proper
        field sanitation, and timely application of suitable pesticides.''')

        st.subheader('Rice as Food')
        st.caption('''
        Rice is a staple food in many cultures and cuisines. It is consumed as whole 
        grains, milled white rice, brown rice, and various rice-based dishes. Rice is 
        a source of  carbohydrates and provides energy to the human body.''')

        st.subheader('Rice Uses')
        st.caption('''
        Apart from being a dietary staple, rice has various uses such as in the production 
        of rice bran oil, rice flour, rice cakes, and even alcoholic beverages. Rice straw 
        is used as animal feed, and rice husks have industrial applications in sectors like
        energy production and building materials.''')



    if crop_name == 'Sorghum':
        st.image(
            'https://cdn.pixabay.com/photo/2014/02/26/13/20/sorghum-275258_1280.jpg',
            caption='Sorghum', width=600)
        st.caption('''
        Sorghum is a versatile cereal crop known for its ability to grow in challenging 
        conditions and its various uses.''')

        st.subheader('Season')
        st.caption('''
        Sorghum is grown as both a Kharif and Rabi crop, depending on the region. In
        India, Kharif sorghum is sown during the monsoon season, from June to July,
        and harvested from September to October. Rabi sorghum is sown during the 
        winter season, from November to December, and harvested from March to April.''')

        st.subheader('Water and Other Nutrient Requirements')
        st.caption('''
        Sorghum is drought-resistant and can grow with relatively lower water requirements
        compared to other crops. However, adequate moisture during the critical growth 
        stages is essential. Nutrient requirements include nitrogen, phosphorus,and 
        potassium, with variations based on soil conditions.''')

        st.subheader('Price Range')
        st.caption('''
        The price of sorghum can vary based on factors such as demand, supply, market 
        conditions, and quality. It is often used as food, fodder, and industrial purposes
        , which can influence its price range.''')

        st.subheader('Top Sorghum Producing States in India')
        st.caption('''
        The top sorghum-producing states in India include Maharashtra, Karnataka, 
        Andhra Pradesh, Telangana, and Tamil Nadu. These states have favorable agro-
        climatic conditions for sorghum cultivation.''')

        st.subheader('Machinery Requirements')
        st.caption('''
        Common agricultural machinery used for sorghum cultivation includes ploughs, 
        harrows, seed drills, tractors, threshers, and other equipment for planting and
        harvesting.  The choice of machinery depends on the scale of cultivation and the
        farming practices.''')

        st.subheader('Fertilizers and Farming Techniques')
        st.caption('''
        Sorghum cultivation requires proper fertilization to achieve good yields. 
        Fertilizers containing nitrogen, phosphorus, and potassium are commonly used. 
        Farming techniques for sorghum involve proper land preparation, timely sowing,
        spacing, and weed  management.''')

        st.subheader('Sorghum Crop Diseases')
        st.caption('''
        Common diseases affecting sorghum include anthracnose, downy mildew, rust, and 
        head smut. Disease management includes crop rotation, use of disease-resistant 
        varieties, and application of appropriate fungicides.''')

        st.subheader('Sorghum as Food')
        st.caption('''
        Sorghum is used as food in various forms, such as whole grains, flour, and 
        traditional dishes. It is often used to make flatbreads, porridge, and snacks. 
        Sorghum is gluten-free and rich in nutrients.''')

        st.subheader('Sorghum Uses')
        st.caption('''
        Apart from being a food source, sorghum has various uses. It is used as animal 
        feed, fodder for livestock, and raw material for industrial purposes. Sorghum 
        can be processed into products like sorghum syrup, biofuels, and even used in
        the production of alcoholic beverages.''')



    if crop_name == 'Soybean':
        st.image(
            'https://e1.pxfuel.com/desktop-wallpaper/213/924/desktop-wallpaper-zenzo-tonzu-soybean.jpg',
            caption='Soybean', width=600)
        st.caption('''
        Soybean is a versatile oilseed crop known for its high protein content and wide
        range of uses.''')

        st.subheader('Season')
        st.caption('''
        Soybean is typically grown as a Kharif crop in India, sown during the monsoon 
        season.The sowing time varies depending on the region, but it generally occurs
        from June to July. The harvesting of soybean usually takes place from September
        to October.''')

        st.subheader('Water and Other Nutrient Requirements')
        st.caption('''
        Soybean requires adequate water during its critical growth stages, especially 
        during flowering and pod formation. Proper irrigation is essential for optimal
        yield. Nutrient requirements for soybean include nitrogen, phosphorus, and 
        potassium, with variations based on soil conditions.''')

        st.subheader('Price Range')
        st.caption('''
        The price of soybean can vary based on factors such as demand, supply, market 
        conditions and quality. It is traded as a commodity and can be influenced by 
        global market dynamics.''')

        st.subheader('Top Soybean Producing States in India')
        st.caption('''
        The top soybean-producing states in India include Madhya Pradesh, Maharashtra, 
        Rajasthan, and Karnataka. These states have favorable agro-climatic conditions 
        for soybean cultivation.''')

        st.subheader('Machinery Requirements')
        st.caption('''
        Common agricultural machinery used for soybean cultivation includes seed drills,
        tractors, planters, cultivators, and harvesters. The choice of machinery depends 
        on the scale of cultivation and the farming practices.''')

        st.subheader('Fertilizers and Farming Techniques')
        st.caption('''
        Soybean cultivation requires proper fertilization to achieve good yields. 
        Fertilizers containing nitrogen, phosphorus, and potassium are commonly used.
        Farming techniques for soybean involve proper land preparation, seed treatment,
        spacing, and weed management.''')

        st.subheader('Soybean Crop Diseases')
        st.caption('''
        Common diseases affecting soybean include rust, leaf spots, root rots, and pod 
        blight. Disease management involves using disease-resistant varieties, crop 
        rotation, and timely application of fungicides.''')

        st.subheader('Soybean as Food')
        st.caption('''
        Soybean is used as a source of high-quality protein and oil in various food 
        products. It can be processed into soybean oil, tofu, soy milk, soy flour, and
        various meat substitutes. Soybean products are widely consumed as part of 
        vegetarian and vegan diets.''')

        st.subheader('Soybean Uses')
        st.caption('''
        Apart from its use as food, soybean has various industrial uses. It is used for
        producing biodiesel, animal feed,and in the manufacturing of products such as
        soy-based ink, plastics, and industrial lubricants.''')

    if crop_name == 'Wheat':
        st.image(
            'https://img.lovepik.com/photo/20211201/large/lovepik-wheat-field-wheat-picture_501339865.jpg',
            caption='Wheat', width=600)
        st.caption('''
        Wheat is one of the most important cereal crops globally, serving as a staple 
        food source for millions of people.''')

        st.subheader('Season')
        st.caption('''
        Wheat is typically grown in two main seasons in India: Rabi and Kharif. The 
        Rabi season starts with the sowing in winter, around October to December, and 
        the harvesting is done in April to June. The Kharif season, which is less 
        common, involves sowing in the rainy season (June to July) and harvesting 
        in the winter months.''')

        st.subheader('Water and Other Nutrient Requirements')
        st.caption('''
        Wheat requires a sufficient amount of water, especially during its critical
        growth stages of tillering, flowering, and grain filling. Proper irrigation 
        management is crucial to prevent water stress. Nutrient requirements for wheat
        include nitrogen, phosphorus, and potassium, with nitrogen being one of the most
        essential nutrients.''')

        st.subheader('Price Range')
        st.caption('''
        The price of wheat can vary based on factors such as demand, supply, market
        conditions, and quality. It is a major commodity in global trade, and prices
        can be influenced by various international and domestic factors.''')

        st.subheader('Top Wheat Producing States in India')
        st.caption('''
        The top wheat-producing states in India include Uttar Pradesh, Punjab, 
        Haryana, Madhya Pradesh, and Rajasthan. These states have favorable agro-
        climatic conditions for wheat cultivation.''')

        st.subheader('Machinery Requirements')
        st.caption('''
        Common agricultural machinery used for wheat cultivation includes ploughs
        , seed drills, tractors, cultivators, harvesters, and threshers. The use of
        modern machinery has significantly increased efficiency and productivity.''')

        st.subheader('Fertilizers and Farming Techniques')
        st.caption('''
        Wheat cultivation requires appropriate fertilization. Nitrogen, phosphorus,
        and potassium are commonly used. Fertilizer application is crucial for 
        achieving high yields. Farming techniques include proper land preparation,
        seed treatment, timely sowing, and weed management.''')

        st.subheader('Wheat Crop Diseases')
        st.caption('''
        Common diseases affecting wheat include rusts, smuts, powdery mildew, and 
        Fusarium head blight. Disease management involves using disease-resistant 
        varieties, crop rotation, and timely application of fungicides.''')

        st.subheader('Wheat as Food')
        st.caption('''
        Wheat is a fundamental food source in various forms. It is used to make 
        bread, pasta, noodles, chapati, and a wide range of baked goods. It provides
        a significant portion of dietary calories and is a staple in many diets 
        worldwide.''')

        st.subheader('Wheat Uses')
        st.caption('''
        Apart from being a primary food source, wheat has various industrial uses.
        It is used for producing wheat flour, which is further processed into starch,
        gluten, and other derivatives used in food and non-food industries.''')


page_names_to_funcs = {
    "Home": intro,
    "What to grow": crop_recommend,
    "Crop Informations": know_crop
}

demo_name = st.sidebar.selectbox("Select Please", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
