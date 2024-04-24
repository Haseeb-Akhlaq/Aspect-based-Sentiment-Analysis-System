import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def aspect_based_sentiment_analysis(text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant trained to perform aspect-based sentiment analysis. Analyze restaurant reviews and provide detailed aspect-based sentiments including entities, attributes, opinion target expressions, and sentiment polarities. For example 'The lava cake dessert was incredible and I recommend it.' In this  Entity (E) is  Restaurant and Attribute (A) is FOOD#QUALITY and Opinion Target Expression (OTE) is lava cake dessert and Sentiment Polarity is Positive. You have to do in the same way as I will give other sentences to you",
                },
                {
                    "role": "user",
                    "content": f"Please analyze the following review for aspect-based sentiment:\n\n'{text}'\nProvide the entities, attributes, opinion target expressions, and sentiment polarities clearly structured that Each point should be at new line",
                },
            ],
        )
        if response.choices:
            result_content = response.choices[0].message.content.strip()
            return result_content
        else:
            return "No completion found in the response."
    except Exception as e:
        return str(e)


def main():
    st.title("Aspect-Based Sentiment Analysis")
    user_input = st.text_area("Enter a review sentence:")
    analyze_button = st.button("Analyze Sentiment")  # Button to trigger analysis

    if analyze_button and user_input:
        result = aspect_based_sentiment_analysis(user_input)
        st.write("Analysis Results:")
        if result:
            st.markdown("### Analysis Results")
            st.markdown(result, unsafe_allow_html=True)
        else:
            st.write("No analysis was performed or there was an error.")


if __name__ == "__main__":
    main()
