import unreal

def listAssetPaths():

    EAL = unreal.EditorAssetLibrary
    
    assetPaths = EAL.list_assets('/Game')
    
    for assetPath in assetPaths: print(assetPath)
    
def getSelectionContentBrowser():

    EUL = unreal.EditorUtilityLibrary
    
    selectedAssets = EUL.get_selected_assets()
    
    for selectedAsset in selectedAssets: print(selectedAsset)
    
def getAllActors():

    #EAS = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    EAS = unreal.EditorActorSubsystem()
    
    actors = EAS.get_all_level_actors()
    
    for actor in actors: print(actor)
    
def getSelectedActors():

    EAS = unreal.EditorActorSubsystem()
    
    selectedActors = EAS.get_selected_level_actors()
    
    for selectedActor in selectedActors: print(selectedActor)
    
def getAssetClass(classType):

    EAL = unreal.EditorAssetLibrary
    
    assetPaths = EAL.list_assets('/Game')
    
    assets = []
    
    for assetPath in assetPaths:
        assetData = EAL.find_asset_data(assetPath)
        assetClass = assetData.asset_class_path
        print(assetClass.asset_name)
        if assetClass.asset_name == classType:
            assets.append(assetData.get_asset())
            
    #for asset in assets: print(asset)
    return assets
    
def getStaticMeshData():

    staticMeshes = getAssetClass('StaticMesh')
    for staticMesh in staticMeshes:
        # assetImportData = staticMesh.get_editor_property('asset_import_data')
        # fbxFilePath = assetImportData.extract_filenames()
        # print(fbxFilePath)
        
        lodGroupInfo = staticMesh.get_editor_property('lod_group')
        print(lodGroupInfo) 
                
def setStaticMeshData():

    if lodGroupInfo == 'None':
            if staticMesh.get_num_lods() == 1:
                staticMesh.set_editor_property('lod_group', 'LargeProp')
                
def getStatcMeshLODData():
    
    PML = unreal.ProceduralMeshLibrary
    staticMeshes = getAssetClass('StaticMesh')
    for staticMesh in staticMeshes:
        staticMeshTriCount = []
        numLODs = staticMesh.get_num_lods()
        
        for i in range(numLODs):
            numSections = staticMesh.get_num_sections(i)
            LODTriCount = 0
            
            for j in range(numSections):
                sectionData = PML.get_section_from_static_mesh(staticMesh, i, j)
                sectionTriCount = len(sectionData[1])/3
                LODTriCount += sectionTriCount
                
            staticMeshTriCount.append(LODTriCount)
            
        staticMeshReductions = [100]
        
        for i in range(1, len(staticMeshTriCount)):
            staticMeshReductions.append(int((staticMeshTriCount[i]/staticMeshTriCount[0]) * 100))
            
        print(staticMesh.get_name())
        print(staticMeshTriCount)
        print(staticMeshReductions)
        print('_______')