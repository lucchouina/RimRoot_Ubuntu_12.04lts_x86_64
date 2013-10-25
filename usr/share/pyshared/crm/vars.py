# Copyright (C) 2008 Dejan Muhamedagic <dmuhamedagic@suse.de>
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# 
# You should have received a copy of the GNU General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

import os, pwd
from singletonmixin import Singleton

def getpwdent():
    try: euid = os.geteuid()
    except Exception, msg:
        common_err(msg)
        return None
    try: pwdent = pwd.getpwuid(euid)
    except Exception, msg:
        common_err(msg)
        return None
    return pwdent
def getuser():
    user = os.getenv("USER")
    if not user:
        try: return getpwdent()[0]
        except: return None
    else:
        return user
def gethomedir():
    homedir = os.getenv("HOME")
    if not homedir:
        try: return getpwdent()[5]
        except: return None
    else:
        return homedir

class Vars(Singleton):
    cib_cli_map = {
    "node": "node",
    "primitive": "primitive",
    "group": "group",
    "clone": "clone",
    "master": "ms",
    "rsc_location": "location",
    "rsc_colocation": "colocation",
    "rsc_order": "order",
    "cluster_property_set": "property",
    "rsc_defaults": "rsc_defaults",
    "op_defaults": "op_defaults",
    "acl_user": "user",
    "acl_role": "role",
    }
    container_tags = ("group", "clone", "ms", "master")
    clonems_tags = ("clone", "ms", "master")
    resource_tags = ("primitive","group","clone","ms","master")
    constraint_tags = ("rsc_location","rsc_colocation","rsc_order")
    constraint_rsc_refs = ("rsc","with-rsc","first","then")
    children_tags = ("group", "primitive")
    nvpairs_tags = ("meta_attributes", "instance_attributes", "utilization")
    defaults_tags = ("rsc_defaults","op_defaults")
    resource_cli_names = ("primitive","group","clone","ms","master")
    constraint_cli_names = ("location","colocation","collocation","order")
    nvset_cli_names = ("property","rsc_defaults","op_defaults")
    op_cli_names = ("monitor", "start", "stop", "migrate_to", "migrate_from","promote","demote","notify")
    ra_operations = ("probe", "monitor", "start", "stop",
       "promote", "demote", "notify", "migrate_to", "migrate_from")
    subpfx_list = {
        "instance_attributes": "instance_attributes",
        "meta_attributes": "meta_attributes",
        "utilization": "utilization",
        "operations": "ops",
        "rule": "rule",
        "expression": "expression",
        "date_expression": "expression",
        "duration": "duration",
        "date_spec": "date_spec",
        "read": "read",
        "write": "write",
        "deny": "deny",
    }
    acl_rule_names = ("read","write","deny")
    acl_spec_map = {
        "xpath": "xpath",
        "ref": "ref",
        "tag": "tag",
        "attribute": "attribute",
    }
    acl_shortcuts = {
        "meta":
            (r"//primitive\[@id='@@'\]/meta_attributes",r"/nvpair\[@name='@@'\]"),
        "params":
            (r"//primitive\[@id='@@'\]/instance_attributes",r"/nvpair\[@name='@@'\]"),
        "utilization":
            (r"//primitive\[@id='@@'\]/utilization",),
        "location":
            (r"//rsc_location\[@id='cli-prefer-@@' and @rsc='@@'\]",),
        "property":
            (r"//crm_config/cluster_property_set",r"/nvpair\[@name='@@'\]"),
        "nodeattr":
            (r"//nodes/node/instance_attributes",r"/nvpair\[@name='@@'\]"),
        "nodeutil":
            (r"//nodes/node/utilization",r"\[@uname='@@'\]"),
        "node":
            (r"//nodes/node",r"\[@uname='@@'\]"),
        "status":
            (r"/cib/status",),
        "cib":
            (r"/cib",),
    }
    lrm_exit_codes = {
        "success": "0",
        "unknown": "1",
        "args": "2",
        "unimplemented": "3",
        "perm": "4",
        "installed": "5",
        "configured": "6",
        "not_running": "7",
        "master": "8",
        "failed_master": "9",
    }
    lrm_status_codes = {
        "pending": "-1",
        "done": "0",
        "cancelled": "1",
        "timeout": "2",
        "notsupported": "3",
        "error": "4",
    }
    node_states = ("online", "offline", "unclean")
    precious_attrs = ("id-ref",)
    time_op_attrs = ("timeout",)
    req_op_attributes = ("name", "id")
    req_sections = ("crm_config", "nodes", "resources", "constraints")
    op_attributes = (
        "interval", "timeout", "requires", "enabled", "role",
        "on-fail", "start-delay", "interval-origin",
        "record-pending", "description",
    )
    rsc_meta_attributes = (
        "allow-migrate", "is-managed", "interval-origin",
        "migration-threshold", "priority", "multiple-active",
        "failure-timeout", "resource-stickiness", "target-role",
        "restart-type", "description",
    )
    clone_meta_attributes = (
        "ordered", "notify", "interleave", "globally-unique",
        "clone-max", "clone-node-max", "clone-state", "description",
    )
    ms_meta_attributes = (
        "master-max", "master-node-max", "description",
    )
    score_types = {'advisory': '0','mandatory': 'INFINITY'}
    boolean_ops = ('or','and')
    binary_ops = ('lt','gt','lte','gte','eq','ne')
    binary_types = ('string' , 'version' , 'number')
    unary_ops = ('defined','not_defined')
    simple_date_ops = ('lt','gt')
    date_ops = ('lt','gt','in_range','date_spec')
    date_spec_names = '''hours monthdays weekdays yearsdays months \
        weeks years weekyears moon'''.split()
    in_range_attrs = ('start','end')
    roles_names = ('Stopped', 'Started', 'Master', 'Slave')
    actions_names = ( 'start', 'promote', 'demote', 'stop')
    node_default_type = "normal"
    node_attributes_keyw = ("attributes","utilization")
    shadow_envvar = "CIB_shadow"

    prompt = ''
    tmpfiles = []
    this_node = os.uname()[1]
    cib_in_use = os.getenv(shadow_envvar)
    homedir = gethomedir()
    if not homedir:
        hist_file = ''
    else:
        hist_file = os.path.join(homedir,".crm_history")
    rc_file = os.path.join(homedir,".crm.rc")
    tmpl_conf_dir = os.path.join(homedir,".crmconf")
    tmpl_dir = "/usr/share/pacemaker/templates"
    pe_dir = "/var/lib/pengine"
    crm_conf_dir = "/var/lib/heartbeat/crm"
    crm_daemon_dir = "/usr/lib/heartbeat"
    crm_daemon_user = "hacluster"
    crm_version = "1.1.6 (Build 9971ebba4494012a93c03b40a2c58ec0eb60f50c)"

    ra_if = None # class interface to RA
    stonithd_metadata = None # stonithd meta data
    pe_metadata = None # PE meta data
    crmd_metadata = None # crmd meta data
    cib_metadata = None # cib meta data
    crm_properties_metadata = None # PE + crmd + cib meta data
    meta_progs = ("crmd","pengine","stonithd","cib")
    crmd_advanced = (
        "dc-version",
        "cluster-infrastructure",
        "crmd-integration-timeout",
        "crmd-finalization-timeout",
        "expected-quorum-votes",
    )

# vim:ts=4:sw=4:et:
