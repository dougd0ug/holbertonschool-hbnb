# **Documentation compilation**

## **1. Introduction**

### **Purpose of the Document**

This section is a technical presentation of diagrams for our project Hbnb. It brings architecture of the project, design decisions and interactions between all layers and classes.

### **Overview of the project**

**Hbnb** project is a simplified version of Airbnb with some utilities :

- Register as an user and update profile
- Looking for some places with prices, location and description
- Rating places and leave comments about it
- Add some amenities associate to places

## **2. High-Level Architecture**

In this high-level architecture diagram, we want to light on the interactions between the 3 layers :

- **Presentation Layer**: This includes the services and API through which users interact with the system.
- **Business Logic Layer**: This contains the models and the core logic of the application.
- **Persistence Layer**: This is responsible for storing and retrieving data from the database.

### **High-level package diagram**

[![](https://mermaid.ink/img/pako:eNptUl1r4zAQ_CtiXxsH23FjW5TAJe3BQaGh5V4Ov-zZG1c0XgVJ7l0a8t-rKE7AtKAH7TC7M_txgFo3BBKiKKq41rxRraxYCPdKHUnBpKMGzVvFZ8IWrb1X2BrshkisDVlih05pfsQ9GXE4FRDi7u4XOzIbrGmxOEM3z55r3gN3QNbaOoHsH2uuaYQKQ--K_g3YC3EjOrIWW7IDtjKEjkJ-Xeue3YAvz1jTKVbWGXTaVHy8WF72VrEv9KhbVY883_z2_sQDO-X2Fytb38AYeg62xtiPjthHV_AqtiZjvQfyzY2l7tHhX7QUuF-nGEWL74xK8RNrbEis0fnp-jF-QzrlftGV4qIonnZkgpSfI0ygNaoB6UxPE-jIdHgKIfisIFxCBdJ_wyWA9-tzdsh_tO4uaUb37SvIDW6tj_pd49cyHMqV4vdHZnXaEsgkS0MNkAf4DzKNb6fzOMnLMo_n6SzLJrD3pGQ-zcoizpN8niSzopwdJ_ARVOPpbV6kcZoURRGXWZ6Ux08-1u28?type=png)](https://mermaid.live/edit#pako:eNptUl1r4zAQ_CtiXxsH23FjW5TAJe3BQaGh5V4Ov-zZG1c0XgVJ7l0a8t-rKE7AtKAH7TC7M_txgFo3BBKiKKq41rxRraxYCPdKHUnBpKMGzVvFZ8IWrb1X2BrshkisDVlih05pfsQ9GXE4FRDi7u4XOzIbrGmxOEM3z55r3gN3QNbaOoHsH2uuaYQKQ--K_g3YC3EjOrIWW7IDtjKEjkJ-Xeue3YAvz1jTKVbWGXTaVHy8WF72VrEv9KhbVY883_z2_sQDO-X2Fytb38AYeg62xtiPjthHV_AqtiZjvQfyzY2l7tHhX7QUuF-nGEWL74xK8RNrbEis0fnp-jF-QzrlftGV4qIonnZkgpSfI0ygNaoB6UxPE-jIdHgKIfisIFxCBdJ_wyWA9-tzdsh_tO4uaUb37SvIDW6tj_pd49cyHMqV4vdHZnXaEsgkS0MNkAf4DzKNb6fzOMnLMo_n6SzLJrD3pGQ-zcoizpN8niSzopwdJ_ARVOPpbV6kcZoURRGXWZ6Ux08-1u28)

## **3. Business Logic Layer**

This section is a presentation of different classes and entities of the project. Every entities have attributes and methods, with relations between them, for the logic of the project.

### **Entities**

#### **1. User Entity**

- Attributes
  - `id: UUID`
  - `first_name: string`
  - `last_name: string`
  - `email: string`
  - `password: String`
  - `admin: Boolean`
  - `created_at: date`
  - `updated_at: date`
- Methods
  - `register_user() : void`
  - `update_user() : void`
  - `delete_user() : void`

#### **2. Place Entity**

- Attributes
  - `id: UUID`
  - `title: string`
  - `description: string`
  - `price: float`
  - `latitude: float`
  - `longitude: float`
- Methods
  - `create_place() : void`
  - `update_place() : void`
  - `delete_place() : void`
  - `list_place() : void`

#### **3. Review Entity**

- Attributes
  - `id: UUID`
  - `user: string`
  - `place: string`
  - `rating: int`
  - `comment: string`
- Methods
  - `create_review() : void`
  - `update_review() : void`
  - `delete_review() : void`
  - `list_review() : void`

#### **4. Amenity Entity**

- Attributes
  - `id: UUID`
  - `name: string`
  - `description: string`
- Methods
  - `create_amenity() : void`
  - `update_amenity() : void`
  - `delete_amenity() : void`
  - `list_amenity() : void`

### **Detailed Class Diagram for Business Logic Layer**

[![](https://mermaid.ink/img/pako:eNp9lFFvmzAUhf-K5adNDVEIJCF-qNS1eYi0TVPXbGqFFHnYodbARhezrMvy33chlGYxCbzg73DNPcc2O5oYISmjScbL8k7xFHgea6FAJlYZTR4-xJrg1ehk9XVxT3axjm3NPCXIarW868YbBaVda55LwkhpQem007D-nCRzrjIXF_jFrQHhKlzkSiP-YUwmue54ApJbKdbcoijwsVOqQvQrVyBTVVoJ66qU8O59xw8Vp1TITB7Rmu1RPIroy8eb28X5jK6sspmbAU5cJqCKJnNHLEAldc0mM9x2NOM4VyV6BKPTfuUQ0LrIeCJdr6e4NXuKM8zrDfZEcPNp8Xn58HghhN59cDmDtnUs1Mq-uM27Qtu-KzQGjnCPhfvFt-Xi-wUH9Q7oWag6FRcDrpROkSt9tBYmxxbsWacgfym5dY06vPXp8MbmG_3PZXOQPe_vdbtfGTFbXR60AzGe1y0kIwUHS8zm-AXPu36NiRHMzCQK26MDmoISlFmo5IDmEvBw45Du6tqY2meZy5gyfBQcfsY01nusKbh-MiZ_LQNTpc-UbXhW4uhgvP05dRSkFhJuTaUtZcE0bCahbEd_U-aPR0M_iHw_GM0n_nwymw7oC2XeeBoNw2g2mgR-NA3DcBLuB_RP82F_GEwn43nk4z0PgmgW7v8Bg8mb0A?type=png)](https://mermaid.live/edit#pako:eNp9lFFvmzAUhf-K5adNDVEIJCF-qNS1eYi0TVPXbGqFFHnYodbARhezrMvy33chlGYxCbzg73DNPcc2O5oYISmjScbL8k7xFHgea6FAJlYZTR4-xJrg1ehk9XVxT3axjm3NPCXIarW868YbBaVda55LwkhpQem007D-nCRzrjIXF_jFrQHhKlzkSiP-YUwmue54ApJbKdbcoijwsVOqQvQrVyBTVVoJ66qU8O59xw8Vp1TITB7Rmu1RPIroy8eb28X5jK6sspmbAU5cJqCKJnNHLEAldc0mM9x2NOM4VyV6BKPTfuUQ0LrIeCJdr6e4NXuKM8zrDfZEcPNp8Xn58HghhN59cDmDtnUs1Mq-uM27Qtu-KzQGjnCPhfvFt-Xi-wUH9Q7oWag6FRcDrpROkSt9tBYmxxbsWacgfym5dY06vPXp8MbmG_3PZXOQPe_vdbtfGTFbXR60AzGe1y0kIwUHS8zm-AXPu36NiRHMzCQK26MDmoISlFmo5IDmEvBw45Du6tqY2meZy5gyfBQcfsY01nusKbh-MiZ_LQNTpc-UbXhW4uhgvP05dRSkFhJuTaUtZcE0bCahbEd_U-aPR0M_iHw_GM0n_nwymw7oC2XeeBoNw2g2mgR-NA3DcBLuB_RP82F_GEwn43nk4z0PgmgW7v8Bg8mb0A)

## **4. Sequence Diagrams**

This section concerns how the dynamics of the website should work with its different layers. So, here are 4 cases of use, and the according uml representation.

### User creation

In this first case, a user requests the right to register himself on the website. So the user layer makes an API call to submit his data, the API validates and process the request to the business logic layer, which will save given user data in the database. The database will return the success or failure of the process to the preceding business logic layer, which returns the same result to the API, and the API informs the user.

[![](https://mermaid.ink/img/pako:eNplUUtPwzAM_iuRz93oa2zNYRIMISFxQENwQLmY1isRbTLyQMC0_06y0Ullt_jz97CdHdS6IeBg6cOTqulGYmuwF2qLxslablE59mTJjJGrh7sxcO2tVGTtvW5lPW7doMNXtCSUUNFpslwGOY8ebIVdx9Yx2x5jQtFK6ww6qQM_cAJ9ZM7ZM3ayQUcMVcMejK5DazARakQO4iGes0f8pGNIxIQaOpPziJVWG2n6g-S_5TD_mpw36ui6JrvVKu4YJw6MGHOinC3GHn0dp764Rdl5Q5BAa2QD3BlPCfRkeowl7IRiTIB7o54E8PBs0LwLEGofNOG8L1r3g8xo374B32BnQ-W38UZ__3lCDamGzEp75YAXVXowAb6DL-BlWkyLsixm6eViNq-yqkzgG3iW5tOyyvOsmOdlVSyK-T6Bn0NuOp2laZ5laVFmizwI8_0vK0rKHA?type=png)](https://mermaid.live/edit#pako:eNplUUtPwzAM_iuRz93oa2zNYRIMISFxQENwQLmY1isRbTLyQMC0_06y0Ullt_jz97CdHdS6IeBg6cOTqulGYmuwF2qLxslablE59mTJjJGrh7sxcO2tVGTtvW5lPW7doMNXtCSUUNFpslwGOY8ebIVdx9Yx2x5jQtFK6ww6qQM_cAJ9ZM7ZM3ayQUcMVcMejK5DazARakQO4iGes0f8pGNIxIQaOpPziJVWG2n6g-S_5TD_mpw36ui6JrvVKu4YJw6MGHOinC3GHn0dp764Rdl5Q5BAa2QD3BlPCfRkeowl7IRiTIB7o54E8PBs0LwLEGofNOG8L1r3g8xo374B32BnQ-W38UZ__3lCDamGzEp75YAXVXowAb6DL-BlWkyLsixm6eViNq-yqkzgG3iW5tOyyvOsmOdlVSyK-T6Bn0NuOp2laZ5laVFmizwI8_0vK0rKHA)

### Place creation

In this second case, a user wants to create a new place announce on the website. So the user layer makes an API call to submit the place data, the API validates and process the request to the business logic layer, which will save given user data in the database. The database will return the success or failure of the process to the preceding business logic layer, which returns the same result to the API, and the API informs the user.

[![](https://mermaid.ink/img/pako:eNplUctu2zAQ_BViTw1gG9TDkcVDgMS-FOjBcNEeCl420lohIi0dkiqaGP73knYcQMmJ5MzOzO7yCI1tCRR4ehmJG9oY7BwOmg_ogmnMATmIX57cFLnffp8CD6M3TN7_sJ1pptQGAz6iJ82ak9P87i7KVfIQa-x78W3bY0OicYTBWBYu9eLDjeZYEqsn3kr8xt60GEggt2LrbBMpsbtoNE-Ko_iarsRP_EviEpVAzVdq_jVjbXlv3HDWfPa89r-jMDqOhz9YTuOlbiOZZlTvQTvqjA_uMldzMaUWZtA504IKbqQZDOQGTE84ahZCQ3iigTSoeG3RPWvQfIqauM0_1g5XmbNj9wRqj72Pr_GQdvL-fR-oI27Jre3IAVRRl2cTUEf4B6qUxaIoy2Ipb1fLqs4S-woqk_mirPM8K6q8rItVUZ1m8HbOlYullHmWyVspyyor6-r0H_lyw18?type=png)](https://mermaid.live/edit#pako:eNplUctu2zAQ_BViTw1gG9TDkcVDgMS-FOjBcNEeCl420lohIi0dkiqaGP73knYcQMmJ5MzOzO7yCI1tCRR4ehmJG9oY7BwOmg_ogmnMATmIX57cFLnffp8CD6M3TN7_sJ1pptQGAz6iJ82ak9P87i7KVfIQa-x78W3bY0OicYTBWBYu9eLDjeZYEqsn3kr8xt60GEggt2LrbBMpsbtoNE-Ko_iarsRP_EviEpVAzVdq_jVjbXlv3HDWfPa89r-jMDqOhz9YTuOlbiOZZlTvQTvqjA_uMldzMaUWZtA504IKbqQZDOQGTE84ahZCQ3iigTSoeG3RPWvQfIqauM0_1g5XmbNj9wRqj72Pr_GQdvL-fR-oI27Jre3IAVRRl2cTUEf4B6qUxaIoy2Ipb1fLqs4S-woqk_mirPM8K6q8rItVUZ1m8HbOlYullHmWyVspyyor6-r0H_lyw18)

### Review submission

In this third case, a user wants to submit a review of a place on the website. So the user layer makes an API call to submit his review, the API validates and process the request to the business logic layer, which will save given user data in the database, bound to the concerned place. The database will return the success or failure of the process to the preceding business logic layer, which returns the same result to the API, and the API informs the user.

[![](https://mermaid.ink/img/pako:eNplUctOwzAQ_BVrTyC1lfNo0_hQCcoFiUNVBAfki0m2qUWzLrbDq-q_YxeCCJzsnfHM7K4PUJkaQYDD5w6pwiutGqtaSXtlva70XpFndw7tELlYXQ-By85pQuduTKOrIXWlvHpUDiVJik7jxSLIRfRgS7XbsbM1vmh8ZbfdY6ud04bOJQU2PBzYCnavdrpWHpmimq2sqQL1SyZp8D7o-2zBbtULsu-giErqufH_nKWhjbbtSfTXtG9_jb6zFA63NxSnix0HMo4o-qQ1Ntp5q3zojlVfrljDCBqraxDedjiCFm2rYgkHSYxJ8FtsUYII11rZJwmSjkETtvlgTNvLrOmaLYiN2rlQdfu4mO_v-0EtUo12aTryIHI-O5mAOMBbLLNJlufZlM_m06JMynwE7yASnk7yMk2TrEjzMptnxXEEH6dcPplyniYJn3GeF0leFsdPtS_D8Q?type=png)](https://mermaid.live/edit#pako:eNplUctOwzAQ_BVrTyC1lfNo0_hQCcoFiUNVBAfki0m2qUWzLrbDq-q_YxeCCJzsnfHM7K4PUJkaQYDD5w6pwiutGqtaSXtlva70XpFndw7tELlYXQ-By85pQuduTKOrIXWlvHpUDiVJik7jxSLIRfRgS7XbsbM1vmh8ZbfdY6ud04bOJQU2PBzYCnavdrpWHpmimq2sqQL1SyZp8D7o-2zBbtULsu-giErqufH_nKWhjbbtSfTXtG9_jb6zFA63NxSnix0HMo4o-qQ1Ntp5q3zojlVfrljDCBqraxDedjiCFm2rYgkHSYxJ8FtsUYII11rZJwmSjkETtvlgTNvLrOmaLYiN2rlQdfu4mO_v-0EtUo12aTryIHI-O5mAOMBbLLNJlufZlM_m06JMynwE7yASnk7yMk2TrEjzMptnxXEEH6dcPplyniYJn3GeF0leFsdPtS_D8Q)

### Places fetching

In this final case, a user wants to fetch through the list of all the places on the website, applying different filters. So the user layer makes an API call to submit his search criteria, the API validates and process the request to the business logic layer, which will request flagged data in the database. The database will return teh list of all concerned places to the preceding business logic layer, which returns the same result to the API, and the API informs the user.

[![](https://mermaid.ink/img/pako:eNplkVFLwzAUhf9KuE8K3UjbbF3zMNANQdjDmPgieYntXVdsk5qkoI79dxNrZcW33HvPOV9ucoZClwgcLL73qArc1rIyshWqk8bVRd1J5cizRTPt3O0fp4373tYKrd3pqi6mo6108lVaFEqokDRbr72dhwyykU1Dbg4Bbh3ZN7JAS0JURY5149DYW6G80HsmBE4e0BUnUmhj0HZalcEy-IWaSL11vAEnI2nq6wZukAk1imf_mQd0vVED5lc9RY2rXQst2dXWDVv4eXgBfj0hT6gcRFCZugTuTI8RtGhaGUo4C0WIAHfCFgVwfyyleRMg1MV7_Pu-aN2ONqP76gT8KBvrq74rpRs_9K9rUJVoNrr3UM5o8hMC_AwfoUznKWPpgi5XiyyPcxbBJ_CYJnOWJ0mcZgnL01WaXSL4-uHS-YLSJI7pklKWxSzPLt_G9cn0?type=png)](https://mermaid.live/edit#pako:eNplkVFLwzAUhf9KuE8K3UjbbF3zMNANQdjDmPgieYntXVdsk5qkoI79dxNrZcW33HvPOV9ucoZClwgcLL73qArc1rIyshWqk8bVRd1J5cizRTPt3O0fp4373tYKrd3pqi6mo6108lVaFEqokDRbr72dhwyykU1Dbg4Bbh3ZN7JAS0JURY5149DYW6G80HsmBE4e0BUnUmhj0HZalcEy-IWaSL11vAEnI2nq6wZukAk1imf_mQd0vVED5lc9RY2rXQst2dXWDVv4eXgBfj0hT6gcRFCZugTuTI8RtGhaGUo4C0WIAHfCFgVwfyyleRMg1MV7_Pu-aN2ONqP76gT8KBvrq74rpRs_9K9rUJVoNrr3UM5o8hMC_AwfoUznKWPpgi5XiyyPcxbBJ_CYJnOWJ0mcZgnL01WaXSL4-uHS-YLSJI7pklKWxSzPLt_G9cn0)
