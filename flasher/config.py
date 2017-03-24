# CHP_FILE_NAME='/home/howie/Downloads/stable-server-b149-Toshiba_4G_MLC.chp'
# CHP_FILE_NAME='/home/howie/Downloads/stable-chip-pro-vu_meter-b3-Toshiba_512M_SLC.chp'
CHP_FILE_NAME='/home/howie/Downloads/stable-chip-pro-blinkenlights-b1-Toshiba_512M_SLC.chp'

AUTO_START_ON_DEVICE_DETECTION = True #When this is true, the test suite will be run automatically when polling detects device. Button input to start runs is disabled
CLICK_TRIGGERS_ALL = True #If any click is equivalent to clicking on all
RUN_NAME="ChipPro 1" #An id that is written to the database tables to identify the batch. See Flash Stats/Browse Stats button in right pane

LOG_DB = 'log.db' # SQLite database of logs. It will be prefixed by the hostname_

#Constants to change behavior. Also see constants in KivyView
SKIP_IDLE_STATE = True # If true, then there won't be an idle state between done and testing
UDEV_RULES_FILE = '/etc/udev/rules.d/flasher.rules'
SORT_DEVICES = True # Whether the device id from the UDEV file (chip_id_hub_xxx) should be sorted on screen. Sort is numeric
SORT_HUBS = True # Whether the hub name from the UDEV file (chip_id_hub_xxx) should be sorted on screen. Sort is alphabetic

#Constants to change appearance
HUBS_IN_COLUMNS = True # if True, there will be one visual column per hub as defined by the UDEV entry: chip-id-hub-mode
SHOW_STATE = True # if True, shows an Idle.., Testing,  Pass/Fail column. With a 49 port hub, you probably want this to be false

SUCCESS_COLOR = [ 0, 1, 0, 1] # GREEN
FAIL_COLOR = [ 1, 0, 0, 1] # RED
ACTIVE_COLOR = [ 1, 1, 1, 1] # we will use WHITE for active
PASSIVE_COLOR = [ 1, 1, 0, 1] # we will use YELLOW for passive
PROMPT_COLOR = [ 1, .4, .3, 1] # we will use ORANGE for prompts
DISCONNECTED_COLOR = [.3, .3, .3, 1] #when device is disconnected
WHITE_COLOR = [ 1, 1, 1, 1]
YELLOW_COLOR = [ 1, 1, 0, 1]
PAUSED_COLOR = [ 1, .5, 0, 1]

VERBOSE = True #whether more details/errors appear in console
