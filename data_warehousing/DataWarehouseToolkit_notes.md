# Notes on Data Warehouse Toolkit (Book)
Authors: Ralph Kimball & Margy Ross (3rd edition)

---
Note: I know I took notes on Ch. 1 of this book, but I can't find them on my Zalando laptop. Find them on my personal computer... (-Kevin, Jun 27, 2023)

---

## Chapter 2: Kimball Dimensional Modeling Overview
Note: This chapter intended to be a reference. Holds info about traditional foundational concepts in Kimball modeling

**General steps to model data**
1. **Gather business requirements** (and ask probing questions + challenge)
2. **Have a collaborative workshop to design a model**
    1. should include data warehouse experts and subject matter experts; data warehouse experts are in charge, but buy-in from business is critical
3. **Design dimensions in 4-step process**
    1. **Select business process** (e.g., "processing an online order" or "registering students for class"). This allows us to focus our scope.
    2. **Declare the grain** (i.e., what does a single fact table row represent? As discussed in Chapter 1, we can view fact table entries as discrete events (e.g., a single order) or as a sequence of events (e.g., steps in an onboarding process), among other paradigms).
       1. It's generally good practice to go for the smallest (most atomic) grain available unless you have a compelling business reason not to.
    3. **Identify dimensions**
       1. Whenever possible, a dimension should be single-valued (i.e., 2 columns - key and value - for a dimension table). This allows maximal flexibility since dimensions can be modified without dependencies on one another.
    4. **Identify facts** - should be relatively simple after grain is determined. But this discussion can also include the additional details in the fact table (e.g., do we include date, and price?)
 4. **Develop Start Schemas & OLAP cubes**
    1. Reminder that star schemas have 1 type of join: the fact table to a single dimension table (in contrast to snowflake schemas)
    2. Reminder that OLAP cubes are sets of pre-aggregated data across certain dimensions that are likely to be of continual interest
       1. For example, income per market, per month, per customer segment. These 3 dimensions have different 'levels' within them and can be combined in a multitude of ways. We pre-calculate all possible combinations and present these as a cube so that queries can just 'look up' the answer rather than re-calculating it every time.
       2. **NOTE:** I am hearing more and more that Kimball's and Inmon's ideas about strict modeling might be less relevant given the abundance of computing and memory resources. See [this article](https://www.holistics.io/blog/the-rise-and-fall-of-the-olap-cube/) for one discussion.



