# Global Temperature Visualization — D3.js Assignment

## Sketches (30%)

Before coding, I created several paper sketches to explore possible visualizations. Quantity and multivariate exploration were prioritized over polish. Each sketch addresses a specific question:

1. **Scatterplot (Time vs. LAT, radius = LATU)**  
   - *Question:* How has global land temperature changed over time, and when was uncertainty higher or lower?  
   - *Why:* The y-axis shows temperature levels, the x-axis shows time, and the circle radius represents uncertainty.

2. **Scatterplot (Time vs. LAT, color = LATU, fixed radius)**  
   - *Question:* Do years with high uncertainty cluster in particular periods?  
   - *Why:* Color encodes uncertainty, letting us trace temperature changes more clearly over time.

3. **Line Chart (Time vs. LOAT)**  
   - *Question:* What is the overall trend in combined land + ocean temperature over the years?  
   - *Why:* Continuous lines emphasize long-term changes and reveal warming patterns.

4. **Line Chart with Rolling Average Overlay (12-month mean)**  
   - *Question:* What long-term trends emerge if we smooth seasonal fluctuations in temperature data?  
   - *Why:* Adding a moving average line makes gradual warming trends easier to see.

5. **Scatterplot with Dual Encoding (Time vs. LAT, radius = LATU, color = LOAT)**  
   - *Question:* How do land and land+ocean temperatures evolve together, and does uncertainty vary by period?  
   - *Why:* Size shows uncertainty while color shows land+ocean temperature, enabling multivariate comparison.

6. **Small Multiples by Decade (LAT vs Time for each decade)**  
   - *Question:* How do temperature and uncertainty patterns differ across decades?  
   - *Why:* Side-by-side plots highlight changes in variability and distribution over time.

---

## Visualization (70%)

<!-- The final interactive visualizations were implemented in **`index.html`** using D3.js: -->

- **Chart 1 (`#chart1`)**: Scatterplot of **Land Average Temperature (y)** vs **Time (x)**, with **circle radius** representing **Uncertainty (LATU)**.  
- **Extra Practice Chart 2 (`#chart2`)**: Scatterplot of **Land Average Temperature (y)** vs **Time (x)**, with **circle color** representing **Uncertainty (LATU)** and a fixed radius. This lets us compare size vs. color encoding.  
- **Extra Practice Chart 3 (`#chart3`)**: Line chart of **Land+Ocean Average Temperature (LOAT)** vs **Time**, with an additional **12-month rolling average** overlay. This highlights long-term warming trends beyond seasonal fluctuations.  

<!-- Tooltips display the exact date, temperature, and uncertainty when hovering over points. Axes and gridlines help interpret values clearly. -->

---

## Extra Credit (+5%)

I added an **optional background image** (e.g., a semi-transparent world map) to **Chart 1**. This image provides geographic context, reminding viewers that the data represent global land temperatures. However, if the image is too saturated, it can distract from the scatterplot marks. To avoid this, I kept the background semi-transparent so that the data remain visually dominant.

---

## How to Run
1. Place `index.html` and `GlobalTemperatures.json` in the same folder.
2. Run a local server (needed because browsers block local JSON loads):  
   - **Python 3:**  
     ```bash
     python -m http.server 8000
     ```  
     Then open [http://localhost:8000](http://localhost:8000) in your browser.
3. Interact with the scatterplots: hover over points to see exact values.

---
## Extra Credit (+5%)

### Why it helps
- The world map reinforces that the dataset is about **global climate patterns**, not just regional values.  
- It adds intuitive **geographic context**, making the chart feel more meaningful and memorable.  
- With low opacity, the image provides context without competing directly with the data marks.

### Why it hinders
- Background imagery can introduce **visual noise** that distracts from the primary variables.  
- If the map were too dark, colorful, or detailed, it would reduce the **legibility** of points and gridlines.  
- Viewers might mistakenly look for **spatial patterns** on the map, even though the chart only encodes time vs. temperature.

To reduce these issues, I used the **Gray Earth raster** (public domain, from Natural Earth) which is neutral and low in detail, and I set the opacity to **~0.18**. This keeps the data marks visually dominant while still providing subtle global context.
