import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import web_server
from esphome.const import CONF_ID

ta_panel_ns = cg.esphome_ns.namespace("ta_panel")
TAPanel = ta_panel_ns.class_("TAPanel", cg.Component, web_server.CustomPage)

CONF_HTML_FILE = "html_file"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(TAPanel),
    cv.Required(CONF_HTML_FILE): cv.file_
})

async def to_code(config):
    html = await cg.read_file(config[CONF_HTML_FILE])
    var = cg.new_Pvariable(config[CONF_ID], html)
    cg.add(var)
    await cg.register_component(var, config)
