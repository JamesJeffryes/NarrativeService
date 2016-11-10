# -*- coding: utf-8 -*-
#BEGIN_HEADER
from NarrativeService.NarrativeManager import NarrativeManager
from NarrativeService.DynamicServiceCache import DynamicServiceCache
#END_HEADER


class NarrativeService:
    '''
    Module Name:
    NarrativeService

    Module Description:
    A KBase module: NarrativeService
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/briehl/NarrativeService"
    GIT_COMMIT_HASH = "4160c20f06ad13594b303bed870832ec5603c5dc"

    #BEGIN_CLASS_HEADER
    def _nm(self, ctx):
        return NarrativeManager(self.config, ctx, self.setAPICache, self.dataPaletteCache)
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.workspaceURL = config['workspace-url']
        self.serviceWizardURL = config['service-wizard']
        self.narrativeMethodStoreURL = config['narrative-method-store']
        self.setAPICache = DynamicServiceCache(self.serviceWizardURL,
                                               config['setapi-version'],
                                               'SetAPI')
        self.dataPaletteCache = DynamicServiceCache(self.serviceWizardURL,
                                                    config['datapaletteservice-version'],
                                                    'DataPaletteService')
        #END_CONSTRUCTOR
        pass


    def list_objects_with_sets(self, ctx, params):
        """
        :param params: instance of type "ListObjectsWithSetsParams"
           (ws_name/ws_id/workspaces - alternative way of defining workspaces
           (in case of 'workspaces' each string could be workspace name or ID
           converted into string). types - optional filter field, limiting
           output list to set of types. includeMetadata - if 1, includes
           object metadata, if 0, does not. Default 0.) -> structure:
           parameter "ws_name" of String, parameter "ws_id" of Long,
           parameter "workspaces" of list of String, parameter "types" of
           list of String, parameter "includeMetadata" of type "boolean"
           (@range [0,1])
        :returns: instance of type "ListObjectsWithSetsOutput" -> structure:
           parameter "data" of list of type "ListItem" (object_info -
           workspace info for object (including set object), set_items -
           optional property listing info for items of set object, dp_info -
           optional data-palette info (defined for items stored in
           DataPalette object).) -> structure: parameter "object_info" of
           type "object_info" (Information about an object, including user
           provided metadata. obj_id objid - the numerical id of the object.
           obj_name name - the name of the object. type_string type - the
           type of the object. timestamp save_date - the save date of the
           object. obj_ver ver - the version of the object. username saved_by
           - the user that saved or copied the object. ws_id wsid - the
           workspace containing the object. ws_name workspace - the workspace
           containing the object. string chsum - the md5 checksum of the
           object. int size - the size of the object in bytes. usermeta meta
           - arbitrary user-supplied metadata about the object.) -> tuple of
           size 11: parameter "objid" of Long, parameter "name" of String,
           parameter "type" of String, parameter "save_date" of type
           "timestamp" (A time in the format YYYY-MM-DDThh:mm:ssZ, where Z is
           either the character Z (representing the UTC timezone) or the
           difference in time to UTC in the format +/-HHMM, eg:
           2012-12-17T23:24:06-0500 (EST time) 2013-04-03T08:56:32+0000 (UTC
           time) 2013-04-03T08:56:32Z (UTC time)), parameter "version" of
           Long, parameter "saved_by" of String, parameter "wsid" of Long,
           parameter "workspace" of String, parameter "chsum" of String,
           parameter "size" of Long, parameter "meta" of mapping from String
           to String, parameter "set_items" of type "SetItems" -> structure:
           parameter "set_items_info" of list of type "object_info"
           (Information about an object, including user provided metadata.
           obj_id objid - the numerical id of the object. obj_name name - the
           name of the object. type_string type - the type of the object.
           timestamp save_date - the save date of the object. obj_ver ver -
           the version of the object. username saved_by - the user that saved
           or copied the object. ws_id wsid - the workspace containing the
           object. ws_name workspace - the workspace containing the object.
           string chsum - the md5 checksum of the object. int size - the size
           of the object in bytes. usermeta meta - arbitrary user-supplied
           metadata about the object.) -> tuple of size 11: parameter "objid"
           of Long, parameter "name" of String, parameter "type" of String,
           parameter "save_date" of type "timestamp" (A time in the format
           YYYY-MM-DDThh:mm:ssZ, where Z is either the character Z
           (representing the UTC timezone) or the difference in time to UTC
           in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500 (EST time)
           2013-04-03T08:56:32+0000 (UTC time) 2013-04-03T08:56:32Z (UTC
           time)), parameter "version" of Long, parameter "saved_by" of
           String, parameter "wsid" of Long, parameter "workspace" of String,
           parameter "chsum" of String, parameter "size" of Long, parameter
           "meta" of mapping from String to String, parameter "dp_info" of
           type "DataPaletteInfo" (This structure is reserved for future
           use.) -> structure:
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN list_objects_with_sets
        ws_id = params.get("ws_id")
        ws_name = params.get("ws_name")
        workspaces = params.get("workspaces")
        types = params.get("types")
        include_metadata = params.get("includeMetadata", 0)
        returnVal = self._nm(ctx).list_objects_with_sets(ws_id=ws_id, ws_name=ws_name,
                                                         workspaces=workspaces, types=types,
                                                         include_metadata=include_metadata)
        #END list_objects_with_sets

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method list_objects_with_sets return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def copy_narrative(self, ctx, params):
        """
        :param params: instance of type "CopyNarrativeParams" (workspaceId -
           optional workspace ID, if not specified then property from
           workspaceRef object info is used.) -> structure: parameter
           "workspaceRef" of String, parameter "workspaceId" of Long,
           parameter "newName" of String
        :returns: instance of type "CopyNarrativeOutput" -> structure:
           parameter "newWsId" of Long, parameter "newNarId" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN copy_narrative
        newName = params['newName']
        workspaceRef = params['workspaceRef']
        workspaceId = params.get('workspaceId', None)
        returnVal = self._nm(ctx).copy_narrative(newName, workspaceRef, workspaceId)
        #END copy_narrative

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method copy_narrative return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def create_new_narrative(self, ctx, params):
        """
        :param params: instance of type "CreateNewNarrativeParams" (app -
           name of app (optional, either app or method may be defined) method
           - name of method (optional, either app or method may be defined)
           appparam - paramters of app/method packed into string in format:
           "step_pos,param_name,param_value(;...)*" (alternative to appData)
           appData - parameters of app/method in unpacked form (alternative
           to appparam) markdown - markdown text for cell of 'markdown' type
           (optional) copydata - packed inport data in format "import(;...)*"
           (alternative to importData) importData - import data in unpacked
           form (alternative to copydata) includeIntroCell - if 1, adds an
           introductory markdown cell at the top (optional, default 0)) ->
           structure: parameter "app" of String, parameter "method" of
           String, parameter "appparam" of String, parameter "appData" of
           list of type "AppParam" -> tuple of size 3: parameter "step_pos"
           of Long, parameter "key" of String, parameter "value" of String,
           parameter "markdown" of String, parameter "copydata" of String,
           parameter "importData" of list of String, parameter
           "includeIntroCell" of type "boolean" (@range [0,1])
        :returns: instance of type "CreateNewNarrativeOutput" -> structure:
           parameter "workspaceInfo" of type "WorkspaceInfo" (Restructured
           workspace info 'wsInfo' tuple: id: wsInfo[0], name: wsInfo[1],
           owner: wsInfo[2], moddate: wsInfo[3], object_count: wsInfo[4],
           user_permission: wsInfo[5], globalread: wsInfo[6], lockstat:
           wsInfo[7], metadata: wsInfo[8], modDateMs:
           ServiceUtils.iso8601ToMillisSinceEpoch(wsInfo[3])) -> structure:
           parameter "id" of Long, parameter "name" of String, parameter
           "owner" of String, parameter "moddate" of type "timestamp" (A time
           in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "object_count" of
           Long, parameter "user_permission" of type "permission" (Represents
           the permissions a user or users have to a workspace: 'a' -
           administrator. All operations allowed. 'w' - read/write. 'r' -
           read. 'n' - no permissions.), parameter "globalread" of type
           "permission" (Represents the permissions a user or users have to a
           workspace: 'a' - administrator. All operations allowed. 'w' -
           read/write. 'r' - read. 'n' - no permissions.), parameter
           "lockstat" of type "lock_status" (The lock status of a workspace.
           One of 'unlocked', 'locked', or 'published'.), parameter
           "metadata" of mapping from String to String, parameter "modDateMs"
           of Long, parameter "narrativeInfo" of type "ObjectInfo"
           (Restructured workspace object info 'data' tuple: id: data[0],
           name: data[1], type: data[2], save_date: data[3], version:
           data[4], saved_by: data[5], wsid: data[6], ws: data[7], checksum:
           data[8], size: data[9], metadata: data[10], ref: data[6] + '/' +
           data[0] + '/' + data[4], obj_id: 'ws.' + data[6] + '.obj.' +
           data[0], typeModule: type[0], typeName: type[1], typeMajorVersion:
           type[2], typeMinorVersion: type[3], saveDateMs:
           ServiceUtils.iso8601ToMillisSinceEpoch(data[3])) -> structure:
           parameter "id" of Long, parameter "name" of String, parameter
           "type" of String, parameter "save_date" of String, parameter
           "version" of Long, parameter "saved_by" of String, parameter
           "wsid" of Long, parameter "ws" of String, parameter "checksum" of
           String, parameter "size" of Long, parameter "metadata" of mapping
           from String to String, parameter "ref" of String, parameter
           "obj_id" of String, parameter "typeModule" of String, parameter
           "typeName" of String, parameter "typeMajorVersion" of String,
           parameter "typeMinorVersion" of String, parameter "saveDateMs" of
           Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN create_new_narrative
        app = params.get('app')
        method = params.get('method')
        appparam = params.get('appparam')
        appData = params.get('appData')
        markdown = params.get('markdown')
        copydata = params.get('copydata')
        importData = params.get('importData')
        includeIntroCell = params.get('includeIntroCell', 0)
        returnVal = self._nm(ctx).create_new_narrative(app, method, appparam, appData, markdown,
                                                       copydata, importData, includeIntroCell)
        #END create_new_narrative

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method create_new_narrative return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def copy_object(self, ctx, params):
        """
        :param params: instance of type "CopyObjectParams" (ref - workspace
           reference to source object, target_ws_id/target_ws_name -
           alternative ways to define target workspace, target_name -
           optional target object name (if not set then source object name is
           used).) -> structure: parameter "ref" of String, parameter
           "target_ws_id" of Long, parameter "target_ws_name" of String,
           parameter "target_name" of String
        :returns: instance of type "CopyObjectOutput" (info - workspace info
           of created object) -> structure: parameter "info" of type
           "ObjectInfo" (Restructured workspace object info 'data' tuple: id:
           data[0], name: data[1], type: data[2], save_date: data[3],
           version: data[4], saved_by: data[5], wsid: data[6], ws: data[7],
           checksum: data[8], size: data[9], metadata: data[10], ref: data[6]
           + '/' + data[0] + '/' + data[4], obj_id: 'ws.' + data[6] + '.obj.'
           + data[0], typeModule: type[0], typeName: type[1],
           typeMajorVersion: type[2], typeMinorVersion: type[3], saveDateMs:
           ServiceUtils.iso8601ToMillisSinceEpoch(data[3])) -> structure:
           parameter "id" of Long, parameter "name" of String, parameter
           "type" of String, parameter "save_date" of String, parameter
           "version" of Long, parameter "saved_by" of String, parameter
           "wsid" of Long, parameter "ws" of String, parameter "checksum" of
           String, parameter "size" of Long, parameter "metadata" of mapping
           from String to String, parameter "ref" of String, parameter
           "obj_id" of String, parameter "typeModule" of String, parameter
           "typeName" of String, parameter "typeMajorVersion" of String,
           parameter "typeMinorVersion" of String, parameter "saveDateMs" of
           Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN copy_object
        ref = params['ref']
        target_ws_id = params.get('target_ws_id')
        target_ws_name = params.get('target_ws_name')
        target_name = params.get('target_name')
        returnVal = self._nm(ctx).copy_object(ref, target_ws_id, target_ws_name, target_name, None)
        #END copy_object

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method copy_object return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def list_available_types(self, ctx, params):
        """
        :param params: instance of type "ListAvailableTypesParams"
           (workspaces - list of items where each one is workspace name of
           textual ID.) -> structure: parameter "workspaces" of list of String
        :returns: instance of type "ListAvailableTypesOutput" (type_stat -
           number of objects by type) -> structure: parameter "type_stat" of
           mapping from String to Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN list_available_types
        workspaces = params.get("workspaces")
        returnVal = self._nm(ctx).list_available_types(workspaces)
        #END list_available_types

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method list_available_types return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
