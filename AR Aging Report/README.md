# **Accounts Receivable (AR) Aging Dashboard**

## **Introduction**
This report provides a comprehensive view of Accounts Receivable (AR) aging, leveraging the power of Power BI for visualization and AWS Redshift for data extraction and transformation. The report offers valuable insights into outstanding customer invoices, categorized by aging buckets, facilitating informed credit control, risk assessment, and collection strategies. Built on the combined strengths of Power BI and AWS, this AR Aging Report serves as a robust and insightful tool for effectively managing accounts receivable and optimizing cash flow.

---

## **Problem Statement**
Managing accounts receivable is critical for maintaining healthy cash flow and minimizing financial risks. However, without a centralized and dynamic view of AR data, businesses often struggle to:
- Track the status of outstanding invoices.
- Identify delinquent accounts and aging trends.
- Allocate resources effectively for collections.
- Make data-driven decisions to improve cash flow.
This report addresses these challenges by providing a clear, interactive, and real-time overview of AR metrics.

---

## **Design Process**
The overall design process I developed together with the data engineers in this project focused on creating a seamless and insightful AR Aging Report. While the data engineers primarily handled the data pipelines and ETL processes in AWS Redshift, I led the design and development of the Power BI report, ensuring it met the needs of stakeholders across finance, credit control, and executive leadership. This collaborative approach allowed us to deliver a robust and user-friendly tool for managing accounts receivable effectively.

### **Wireframing**
Using Power BI, I developed high-fidelity wireframes with interactive elements to simulate the user experience for key report pages and user flows. These wireframes focused on:
- Clear information hierarchy, especially in differentiating aging buckets and delinquency metrics.
- Intuitive navigation patterns, including filters and slicers for dynamic exploration.
- Strategic placement of key visuals (e.g., bar charts, tables, and KPIs) to highlight critical insights.


### **Visual Design**
The visual design approach centered on creating a professional and data-driven aesthetic that would appeal to both technical and non-technical users. Key elements included:
- A consistent color palette aligned with the organization’s branding, using color coding to differentiate aging buckets and statuses.
- Clear typography guidelines for headers, labels, and data points to ensure readability.
- Bookmarked tabs for ease of navigation around the report.
- Visual cues to distinguish between consolidated and project-level metrics.

### **Report Content**
#### **Page 1: Overview**
- Provides a high-level overview of the report.
- Highlights key findings, trends, and insights at a glance.
  
#### **Page 2: Summary**
This page contains summarized matrix and tables for all KPIs, analyzed by:
- **Status of Accounts**
- **SBU (Strategic Business Unit)**
- **Product**
- **Product Type**

The following reports are included:

1. **Aging of Receivables**:
   - Tracks the movement of contract count by their account statuses between the selected month and the previous month.
   - Includes a summarized comment section highlighting **good** and **bad** movements of accounts.

2. **Outstanding Balance**:
   - Displays the total outstanding balance of all accounts, broken down by **SBU** and **Product**.

3. **Status Summary of Accounts**:
   - Provides a breakdown of the total number of accounts per account status, categorized by **SBU** and **Product**.

4. **Product Delinquency Rate**:
   - Shows the delinquency rate by **SBU** and **Product**.

5. **Delinquency Summary**:
   - Summarizes the total delinquency and outstanding balance by **SBU** and **Product**.

6. **Aged Delinquent Accounts**:
   - Displays delinquent accounts across multiple years for a historical perspective.

7. **Aged Receivable Equity**:
   - Presents a summary of aged receivable equities.

#### **Page 3: Customizable Table**
- Features a **dynamic and customizable table**.
- Allows users to select specific **analysis dimensions** (e.g., SBU, Product, Account Status) and **metrics** (e.g., Contract Count, Outstanding Balance, Delinquency Rate) as defined in the report.
- Enables tailored insights based on user preferences.
  
--- 

## **Implementation and Impact**
Through collaboration with my team and the stakeholders, we:
- Built an ETL pipeline using AWS Redshift to ensure real-time data updates and scheduled automatic refreshes in Power BI.
- Designed interactive dashboards with filters, slicers, and drill-through functionality for dynamic exploration.
- Published the report to Power BI Service with role-based access control for secure stakeholder access.
- Delivered a centralized, real-time view of AR aging, enabling faster identification of delinquent accounts and aging trends.
- Improved decision-making for credit control and collections, enhancing cash flow management through actionable insights.

---

## **Lessons Learned**
### **Challenges**:
- Ensuring data consistency across multiple sources.
- Optimizing query performance for large datasets in AWS Redshift.
### **Successes**:
-	Delivering a user-friendly and insightful tool for stakeholders.
-	Reducing manual effort in AR reporting and analysis.
###	**Future Improvements**:
- Incorporate predictive analytics to forecast delinquency risks.
- Expand the report to include additional financial metrics.

