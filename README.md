# stormwater_pond_model

This repository includes a water balance model and a pollutant mass balance model that use stochastic approaches to understand stormwater pond water and pollutant dynamics. The models show how steady-state analytical solutions for water depth and pollutant mass PDFs in stormwater ponds are validated by dynamic stochastic processes.

** Lee et al. (2026), Hydrologic and biogeochemical controls on stochastic water and pollutant dynamics in stormwater ponds, Journal of Hydrology, 10.1016/j.jhydrol.2026.136468 **

The code was implemented in Python 3.12. The following three scripts form the main structure of the work. It should be noted that simulation results for each run will differ slightly due to the stochastic nature. Large datasets (modeled data reported in the paper) are available on Zenodo. The field data including water depth, inflow and outflow events are also attached.
1.	“pondwater balance AP (CP)” – generate water depth, inflow, and outflow.
Input: hydrological parameters mentioned in the paper
Output: analytical solutions of water depth PDFs, modeled water depth time series and PDFs, inflow, and outflow, and cumulative errors compared to field data
2.	“pondmass balance AP (CP)” – generate pollutant mass time series in the stormwater ponds.
Input: pollutant and hydrologic parameters mentioned in the paper
Output: analytical solutions of pollutant mass PDFs, modeled pollutant mass time series and PDFs
3.	“cumulative error for results in the paper” – supports the findings of this study
Input: modeled data (water depth, inflow, outflow)
Output: cumulative errors reported in this study

If you have any questions while using this code, please contact the author at lee04304@umn.edu.
