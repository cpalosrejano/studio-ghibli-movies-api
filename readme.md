# Studio Ghibli Movies API
This is an open source and free API to fetch every studio ghibli movie detail

[Live here]("https://studio-ghibli-movies-api.vercel.app")

---

### What is SGMA?

This API was created in order to have the details of all Studio Ghibli movies updated to date.

The API offers the details available in different languages, and offers for each country the possibility to finding the streaming platform where you can watch the movie, as well as where you can listen to its soundtrack.

You can see how I implement this API in my own Android App published in  [Google Play]("https://play.google.com/store/apps/details?id=io.kikiriki.sgmovie")

---

### Documentation
You can see the endpoints definitions
- [Swagger]("https://studio-ghibli-movies-api.vercel.app/docs")
- [Redocly]("https://studio-ghibli-movies-api.vercel.app/redoc")

---

### Dependencies
The API is built using Python and FastAPI
- Install python
- Install fastapi
- Install uvicorn

---

### How to add a new translation
- Create a folders structure inside of translation (for example ``fr/LC_MESSAGES``)
- Create or copy a ``messages.po`` file and translate the ``msgstr`` chain
- To build the translations, just run the following command: ``pybabel compile -f -d translations``

---

### How to run in local
Execute the following command to run the API in your computer

``uvicorn main:app --reload``

The API will be available in

``http://127.0.0.1:8000``

---

### How to deploy to Vercel
You have two way to deploy to vercel:

- **Via terminal:**
    - Install vercel with ``npm -i -g vercel``
    - Use ``vercel login`` to link your vercel account to
    - Use ``vercel .`` in your terminal and follow the instructions to deploy

- **Via vercel website:**
    - Just login to your vercel account and deploy your repository by following the instructions

---