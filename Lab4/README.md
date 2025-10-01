
# D3 Scatterplot (Global Temperatures)

A simple D3 v7 scatterplot that visualizes global temperature data with interactive axis toggles and tooltips. The code uses **linear** x/y scales and explicitly updates circle positions via `cxScale(d.time)` and `cyScale(...)`, per the assignment requirements.

---

## What functions does the code support?

### Data & frame utilities
- **`parseYYYYMMDD(n)`**  
  Converts an integer date like `18500101` into a JavaScript `Date` object.

- **`setupFrame(svgSel)`**  
  Sets up the SVG viewBox, margins, and returns the chart group plus inner width/height.

### Scales, axes, and rendering
- **`createScales(data)`**  
  Initializes:  - `cxScale`: `d3.scaleLinear()` mapping numeric `YYYYMMDD` → x pixels  - `rScale`: `d3.scaleSqrt()` mapping `LOATU` → circle radius  - `colorScale`: `d3.scaleQuantize()` mapping `LATU` → fill color buckets  *(Note: `cyScale` is created per Y field inside `updateYAxis`.)*

- **`setupAxes()`**  
  Creates axis groups, labels, and the **x-grid** using `cxScale`.

- **`updateYAxis(dataField, isAnimated = false)`**  
  Creates/updates:  - `cyScale`: `d3.scaleLinear().nice()` for `LAT` or `LOAT`  - Left y-axis & label text  - y-grid lines  - Bottom x-axis (formats numeric `YYYYMMDD` ticks as years)  Repositions circles explicitly with:
  ```js
  .attr("cx", d => cxScale(d.time))
  .attr("cy", d => cyScale(d[dataField]))
  ```
  Optional transition when `isAnimated = true`.

- **`drawScatterplot()`**  
  Binds data and draws circles with radius, position, and color. Adds tooltips that show date, LAT, LOAT, and LOATU.

### UI controls
- **`showAssignment()`**  
  Resets to LAT on the y-axis (no animation), hides extra-credit controls.

- **`showExtraCredit()`**  
  Shows extra-credit controls and resets to LAT with animation. Two buttons call `updateYAxis('LAT', true)` or `updateYAxis('LOAT', true)`.

---
## How to Run
1. Run a local server (needed because browsers block local JSON loads):  
   - **Python 3:**  
     ```bash
     python -m http.server 8000
     ```  
     Then open [http://localhost:8000](http://localhost:8000) in your browser.
