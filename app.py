import streamlit as st
from agents import (
    fetch_movie_data,
    analysis_agent,
    generate_pdf
)
st.set_page_config(page_title="🎬 Movie Intelligence System")
st.title("🎬 Multi-Agent Movie Intelligence System")

movie_title = st.text_input("Enter Movie Title")
user_question = st.text_area("Ask a question about the movie")

if st.button("Analyze Movie") and movie_title:
    try:
        # Step 1: Fetch movie data
        with st.spinner("Fetching movie data..."):
            movie_data = fetch_movie_data(movie_title)

        if movie_data.get("Response") == "False":
            st.error("Movie not found!")
        else:
            st.success("Movie data fetched successfully!")

            with st.expander("Show Raw Movie Data"):
                st.json(movie_data)

            # Step 2: LLM Analysis
            with st.spinner("Analyzing movie..."):
                prompt = f"""
Movie Title: {movie_title}

Movie Data:
{movie_data}

User Question:
{user_question}

Generate a professional movie analysis including:
- Plot summary
- Director & cast
- Genre and release year
- Ratings
- Answer the user question clearly
"""
                response = analysis_agent.run(prompt)
                summary = response.content

            st.subheader("🎥 Movie Analysis Summary")
            st.write(summary)

            # Step 3: Generate PDF (DIRECT TOOL CALL)
            with st.spinner("Generating PDF..."):
                pdf_file = generate_pdf(summary)

            st.success("PDF generated successfully!")

            st.download_button(
                label="📥 Download PDF Report",
                data=open(pdf_file, "rb"),
                file_name=pdf_file,
                mime="application/pdf"
            )

    except Exception as e:
        st.error(f"Error: {e}")