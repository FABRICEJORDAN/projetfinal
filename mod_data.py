
""" Data module."""
import pandas as pd

def pollution():
    po = pd.read_csv('pollution.csv',sep=";")
    #suppression de la derniere colonne et des autres colonnes qu'on utilisera pas pour la visualisation pour rendre plus fluide 
    # l'affichages des données utilisés pour le dashboard
    po = po.iloc[:, :-1]
    po = po.drop(columns=['City','State','ZipCode','TaxParcelIdentificationNumber','CouncilDistrictCode','Neighborhood',
                        'DefaultData', 'Comments','ComplianceStatus', 'Outlier','DataYear','NumberofFloors','PropertyGFATotal'
                        ,'PropertyGFAParking','PropertyGFABuilding(s)','ListOfAllPropertyUseTypes','LargestPropertyUseTypeGFA',
                        'SecondLargestPropertyUseTypeGFA','ThirdLargestPropertyUseTypeGFA','YearsENERGYSTARCertified',
                        'ENERGYSTARScore','LargestPropertyUseType','NaturalGas(therms)','SiteEUI(kBtu/sf)','SiteEUIWN(kBtu/sf)',
                        'SourceEUI(kBtu/sf)','SourceEUIWN(kBtu/sf)','Electricity(kWh)','SecondLargestPropertyUseType',
                        'ThirdLargestPropertyUseType'])
    #Changer le type de certaines colonnes en string
    po['OSEBuildingID'] = po['OSEBuildingID'].apply(str)
    po['YearBuilt'] = po['YearBuilt'].apply(str)
    # Changer le type number of building en int
    po['NumberofBuildings'] = po['NumberofBuildings'].fillna(0)
    po['NumberofBuildings'] = po['NumberofBuildings'].apply(int)
    # Remplacer les valeurs non renseigné dans les colonnes par la moyenne des valeurs positives
    po['SiteEnergyUse(kBtu)'].fillna(po[po['SiteEnergyUse(kBtu)'] >= 0]['SiteEnergyUse(kBtu)'].mean(), inplace=True) 
    po['SiteEnergyUseWN(kBtu)'].fillna(po[po['SiteEnergyUseWN(kBtu)'] >= 0]['SiteEnergyUseWN(kBtu)'].mean(), inplace=True)
    po['SteamUse(kBtu)'].fillna(po[po['SteamUse(kBtu)'] >= 0]['SteamUse(kBtu)'].mean(), inplace=True)
    po['Electricity(kBtu)'].fillna(po[po['Electricity(kBtu)'] >= 0]['Electricity(kBtu)'].mean(), inplace=True)
    po['NaturalGas(kBtu)'].fillna(po[po['NaturalGas(kBtu)'] >= 0]['NaturalGas(kBtu)'].mean(), inplace=True)
    po['TotalGHGEmissions'].fillna(po[po['TotalGHGEmissions'] >= 0]['TotalGHGEmissions'].mean(), inplace=True)
    po['GHGEmissionsIntensity'].fillna(po[po['GHGEmissionsIntensity'] >= 0]['GHGEmissionsIntensity'].mean(), inplace=True)
    # Recupere uniquement les lignes contenant les valeurs positives des colonnes qui contiennent les valeurs négatives. une fonction a permis d'identifier ces colonnes
    # C'est aussi une manière de se débarasser des valeurs négatives pour éviter d'introduire des données incorrectes dans l analyse. .
    po = po[po['Electricity(kBtu)'] >= 0]
    po = po[po['TotalGHGEmissions'] >= 0]
    po = po[po['GHGEmissionsIntensity'] >= 0]
        
    return po