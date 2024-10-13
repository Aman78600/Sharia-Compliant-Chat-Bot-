import streamlit as st
import time
import base64

################################################################################################

# Import necessary libraries
import google.generativeai as genai

# Configure the GenAI API
genai.configure(api_key='AIzaSyBgEWO0_xIuVPUWDQuQVvs8v3KtVHJY-7s')

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

data="""

1. مبادئ التمويل الإسلامي
التمويل الإسلامي يقوم على مجموعة من المبادئ المستمدة من الشريعة الإسلامية. أحد هذه المبادئ الرئيسية هو حظر الربا (الفوائد).

Islamic finance operates on principles derived from Islamic Sharia law,
with the prohibition of riba (interest) being one of its fundamental principles.
Instead of earning money through interest, financial transactions in Islamic finance must involve profit-sharing or asset-based transactions.
The focus is on equitable risk-sharing between all parties involved, ensuring fairness and justice in financial dealings.
This promotes a more ethical and sustainable financial system that avoids exploitation and ensures everyone benefits fairly from economic activities.

---

2. الاستثمار في الأصول الحقيقية
الاستثمار في الأصول الملموسة هو حجر الزاوية في التمويل الإسلامي. يجب أن تستند جميع المعاملات إلى الأصول الفعلية وليس على المضاربات المالية.

Investing in tangible, real assets is a core principle in Islamic finance.
Transactions must be linked to real economic activities, avoiding speculative or uncertain ventures (gharar). 
This contrasts with conventional finance, where speculative instruments like derivatives can be common. 
Islamic investments are often in assets like real estate, businesses, or infrastructure projects that contribute to the overall economy. 
This approach promotes stability and ensures that financial activities contribute positively to society and the economy.

---

3. الصكوك كبديل للسندات التقليدية
الصكوك هي إحدى الأدوات المالية الأكثر شيوعًا في التمويل الإسلامي. على عكس السندات التقليدية، تعتمد الصكوك على الملكية الحقيقية للأصول.

Sukuk, often referred to as Islamic bonds, are a popular financial instrument in Islamic finance. 
Unlike conventional bonds, which pay interest, sukuk represent partial ownership in an asset or project. 
The returns to sukuk holders come from the profit generated by these assets, making the investment Shariah-compliant. 
Sukuk are increasingly used by governments and corporations globally, offering investors a way to participate in ethical financing while complying with Islamic principles. 
This has contributed to the rapid growth of the sukuk market worldwide.

---

4. التمويل بالمشاركة والمضاربة
المشاركة والمضاربة هما من العقود الأساسية في التمويل الإسلامي. تعتمد هذه العقود على تقاسم الأرباح والخسائر بين الأطراف.

*Shariah*-compliant contracts such as musharakah (partnership) and mudarabah (profit-sharing) are central to Islamic finance. 
In musharakah, all partners contribute capital and share profits and losses according to a pre-agreed ratio. In mudarabah, 
one party provides capital while the other contributes expertise, with profits shared but losses borne by the investor. 
These arrangements ensure ethical and fair collaboration between parties, fostering a spirit of cooperation and mutual benefit in business ventures.

---

5. البنوك الإسلامية ودورها
تلعب البنوك الإسلامية دورًا حيويًا في تقديم الخدمات المالية المتوافقة مع الشريعة الإسلامية. هذه البنوك تختلف عن البنوك التقليدية في العديد من الجوانب.

Islamic banks play a crucial role in providing Shariah-compliant financial services. 
Unlike conventional banks, they do not charge or pay interest. Instead, they operate on profit-sharing, leasing, and trade-based contracts. 
For instance, *Murabaha* involves the bank buying goods and selling them to the customer at a profit, rather than giving a loan with interest. 
Islamic banks also provide products like *Ijara* (leasing) and *Istisna* (construction financing), promoting ethical financial practices that comply with Islamic principles.

---

6. الأسهم المتوافقة مع الشريعة
تعتبر الأسهم المتوافقة مع الشريعة الإسلامية من أهم أدوات الاستثمار في التمويل الإسلامي. يتم فحص الشركات لضمان أن أنشطتها متوافقة مع الشريعة.

Shariah-compliant stocks are an important part of Islamic finance investment strategies. 
Companies are screened to ensure they do not engage in prohibited activities such as alcohol, gambling, or interest-based lending. 
Moreover, these companies must adhere to certain financial ratios to ensure compliance with Islamic law. 
Investors can participate in Islamic equity funds or portfolios that are structured to invest only in Shariah-compliant businesses, 
promoting ethical investments that align with both profitability and religious values.

---

7. دور التكنولوجيا المالية في التمويل الإسلامي
التكنولوجيا المالية (Fintech) لها تأثير كبير على صناعة التمويل الإسلامي. تقدم حلولاً مبتكرة تجعل التمويل الإسلامي أكثر سهولة وفعالية.

Islamic fintech is transforming the delivery of Shariah-compliant financial services by offering innovative solutions. 
From digital banking and mobile payments to peer-to-peer lending and blockchain, fintech is making Islamic finance more accessible and efficient. 
These advancements not only streamline processes but also ensure greater transparency and security, which aligns with the core principles of Islamic finance. 
The growth of Islamic fintech is particularly strong in regions like Southeast Asia and the Middle East, where demand for ethical finance is high.

---

8. اتجاهات السوق في التمويل الإسلامي
التمويل الإسلامي يشهد نمواً سريعاً في جميع أنحاء العالم. المناطق التي تشهد أكبر نمو هي الشرق الأوسط، جنوب شرق آسيا، وأفريقيا.

The Islamic finance sector is growing rapidly worldwide, particularly in the Middle East, Southeast Asia, and Africa. 
The demand for Shariah-compliant financial products, such as Islamic banking, sukuk, and Islamic insurance (*Takaful*), is increasing. 
More non-Muslim countries are also showing interest in Islamic finance as a means to attract investment. 
This trend is supported by the global shift towards ethical finance, as Islamic finance principles align well with the growing demand 
for socially responsible and sustainable investments.

---

### 9. التحديات التي تواجه التمويل الإسلامي
على الرغم من النمو السريع، يواجه التمويل الإسلامي العديد من التحديات. من بين هذه التحديات توحيد المعايير والتشريعات المختلفة في الدول.

Despite the rapid growth of Islamic finance, it faces several challenges. 
One of the main hurdles is the lack of standardized regulations across different countries. 
This can lead to discrepancies in the application of Islamic finance principles, making cross-border transactions complex. 
Another challenge is the need for more professionals trained in Islamic finance, as well as the lack of consumer awareness 
about the benefits of Shariah-compliant financial products. 
Addressing these issues will be key to the continued growth and development of the Islamic finance sector.

---

10. مستقبل التمويل الإسلامي
مستقبل التمويل الإسلامي يبدو واعدًا مع تزايد الطلب على المنتجات المالية المتوافقة مع الشريعة. الابتكارات التقنية ستلعب دورًا كبيرًا في المستقبل.

The future of Islamic finance looks promising as demand for Shariah-compliant financial products continues to grow. 
Innovations in fintech, blockchain, and artificial intelligence are expected to play a significant role in shaping the future of Islamic finance. 
These technologies will improve efficiency, transparency, and accessibility, making Islamic financial services more widely available. 
As the global economy moves towards ethical and sustainable finance, Islamic finance is well-positioned to become a key player in the financial world.

"""



index_of_data="""
1. Principles of Islamic Finance---
2. Investment in Real Assets---
3. ukuk as an Alternative to Bonds---
4. Partnership and Profit-Sharing Contracts---
5. Role of Islamic Banks---
6. Shariah-Compliant Stocks---
7. Islamic Fintech Innovations---
8. Global Market Trends in Islamic Finance---
9. Challenges in Islamic Finance---
10. Future of Islamic Finance
"""



# Function to ask a question based on file content
def ask_question(index_of_data, question):
    # Add file content as context and append the question
    prompt = f""" this is a index page =>###{index_of_data}###. \n\n i want that topic number whar i found this {question} answer.
      (give me only topic number only number not more than it.)
    """
    
    # Get model response
    response = model.generate_content(prompt)
    try:
        response_index=int(response.text)
        list_of_data=data.split('---')
        final_data=list_of_data[response_index-1]
        new_prompt=f"read this data {final_data} and give me answer of this {question}. and give first tow line in arabinc. and then english.  you also add some actra information but not more.\n"

        answer=model.generate_content(new_prompt)
        # Return the answer generated by the model
        return answer.text
    except:
        return "I don't know! \nask me something else."
# ################################################################################################


st.set_page_config(
    page_title="Principles of Islamic",  # Title of the browser tab
    page_icon="inverted_image.jpg",
    
)
 # Save the inverted image if needed

st.markdown(
    """
    <style>
    /* Change all font colors to blue */
    * {
        color: white !important;
    }

    /* Optionally, you can add more styles here */
    </style>
    """,
    unsafe_allow_html=True
)
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('Islamic mosque with black background vector 07 free download.jpeg') 



# Hide the Streamlit menu and footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
   
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)


st.header('Sharia-Compliant Chat Bot!')

question=st.text_input('Ask me a question..')

# Function to update Streamlit output in real-time
def speak_and_print(text_,question):
    # st.write(question)
    output_placeholder = st.empty()
    t = '..'
    for i in text_:
        t = t[:-2]+i+t[-2:]
        output_placeholder.write(t)
        time.sleep(0.05)
    # output_placeholder.write('')
    # st.write(text_)

if st.button('Go'):
    answer = ask_question(index_of_data, question)
    # print(f"Answer: {answer}")
    speak_and_print(answer,question)
