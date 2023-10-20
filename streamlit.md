---
marp: true
theme: default
paginate: true

---

# Streamlit

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

---

Run it with streamlit run:

streamlit run your_script.py [-- script args]

---

- Streamlit apps are Python scripts that run from top to bottom
- Every time a user opens a browser tab pointing to your app, the script is re-executed
- As the script executes, Streamlit draws its output live in a browser
- Scripts use the Streamlit cache to avoid recomputing expensive functions, so updates happen very fast
- Every time a user interacts with a widget, your script is re-executed and the output value of that widget is set to the new value during that run.
- Streamlit apps can contain multiple pages, which are defined in separate .py files in a pages folder.

---

![height:400px center](imgs/app_model.png)

---