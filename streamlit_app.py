import streamlit as st

from solution.solution import (
    batch_compare,
    call_openai,
    call_openai_mini,
    compare_models,
    format_comparison_table,
)


st.set_page_config(page_title="LLM API Lab UI", page_icon="🤖", layout="wide")
st.title("LLM API Foundation - Streamlit UI")
st.caption("Giao dien cho cac ham trong solution/solution.py")


tab_single, tab_compare, tab_batch, tab_chat = st.tabs(
    ["Single Call", "Compare Models", "Batch Compare", "Chatbot"]
)


with tab_single:
    st.subheader("Goi tung model")
    prompt_single = st.text_area(
        "Nhap prompt", height=140, placeholder="Vi du: Giai thich top_p va temperature"
    )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Goi GPT-4o", use_container_width=True):
            if not prompt_single.strip():
                st.warning("Vui long nhap prompt.")
            else:
                with st.spinner("Dang goi GPT-4o..."):
                    response, latency = call_openai(prompt_single)
                st.success(f"Latency: {latency:.3f}s")
                st.write(response)
    with col2:
        if st.button("Goi GPT-4o-mini", use_container_width=True):
            if not prompt_single.strip():
                st.warning("Vui long nhap prompt.")
            else:
                with st.spinner("Dang goi GPT-4o-mini..."):
                    response, latency = call_openai_mini(prompt_single)
                st.success(f"Latency: {latency:.3f}s")
                st.write(response)


with tab_compare:
    st.subheader("So sanh GPT-4o vs GPT-4o-mini")
    prompt_compare = st.text_area(
        "Nhap prompt de so sanh", height=120, key="compare_prompt"
    )
    if st.button("So sanh", type="primary"):
        if not prompt_compare.strip():
            st.warning("Vui long nhap prompt.")
        else:
            with st.spinner("Dang so sanh 2 model..."):
                result = compare_models(prompt_compare)
            st.metric("GPT-4o latency", f"{result['gpt4o_latency']:.3f}s")
            st.metric("Mini latency", f"{result['mini_latency']:.3f}s")
            st.metric("GPT-4o cost estimate", f"${result['gpt4o_cost_estimate']:.6f}")
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("**GPT-4o response**")
                st.write(result["gpt4o_response"])
            with col_b:
                st.markdown("**GPT-4o-mini response**")
                st.write(result["mini_response"])


with tab_batch:
    st.subheader("Batch compare")
    prompts_text = st.text_area(
        "Nhap nhieu prompt, moi dong 1 prompt",
        height=180,
        placeholder="Prompt 1\nPrompt 2\nPrompt 3",
    )
    if st.button("Chay batch compare", use_container_width=True):
        prompts = [line.strip() for line in prompts_text.splitlines() if line.strip()]
        if not prompts:
            st.warning("Vui long nhap it nhat 1 prompt.")
        else:
            with st.spinner("Dang chay batch compare..."):
                results = batch_compare(prompts)
                table_text = format_comparison_table(results)
            st.markdown("**Bang ket qua**")
            st.code(table_text)
            st.markdown("**Du lieu chi tiet**")
            st.json(results)


with tab_chat:
    st.subheader("Chatbot (giu toi da 3 luot)")
    st.caption(
        "UI nay tai hien logic tu streaming_chatbot: luu history va cat con 3 message gan nhat."
    )

    if "history" not in st.session_state:
        st.session_state.history = []

    user_msg = st.chat_input("Nhap tin nhan...")
    if user_msg:
        st.session_state.history.append({"role": "user", "content": user_msg})
        trimmed_messages = st.session_state.history[-3:]

        with st.spinner("Assistant dang tra loi..."):
            response_text, _ = call_openai(trimmed_messages[-1]["content"])

        st.session_state.history.append({"role": "assistant", "content": response_text})
        st.session_state.history = st.session_state.history[-3:]

    for msg in st.session_state.history:
        with st.chat_message("assistant" if msg["role"] == "assistant" else "user"):
            st.write(msg["content"])

    if st.button("Xoa lich su chat"):
        st.session_state.history = []
        st.rerun()
