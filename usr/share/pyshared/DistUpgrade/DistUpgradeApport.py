
import os
import os.path
import logging
import subprocess
import sys
import gettext
import errno

APPORT_WHITELIST = {
    "apt.log": "Aptlog",
    "apt-term.log": "Apttermlog",
    "apt-clone_system_state.tar.gz": "Aptclonesystemstate.tar.gz",
    "history.log": "Historylog",
    "lspci.txt": "Lspcitxt",
    "main.log": "Mainlog",
    "term.log": "Termlog",
    "screenlog.0": "Screenlog",
    "xorg_fixup.log": "Xorgfixup"
    }


def _apport_append_logfiles(report, logdir="/var/log/dist-upgrade/"):
    dirname = 'VarLogDistupgrade'
    for fname in APPORT_WHITELIST:
        f = os.path.join(logdir, fname)
        if not os.path.isfile(f) or os.path.getsize(f) == 0:
            continue
        ident = dirname + APPORT_WHITELIST[fname]
        report[ident] = (open(f), )

def apport_crash(type, value, tb):
    logging.debug("running apport_crash()")
    try:
        from apport_python_hook import apport_excepthook
        from apport.report import Report
    except ImportError, e:
        logging.error("failed to import apport python module, can't report bug: %s" % e)
        return False
    # we pretend we are update-manager
    sys.argv[0] = "/usr/bin/update-manager"
    apport_excepthook(type, value, tb)
    # now add the files in /var/log/dist-upgrade/*
    if os.path.exists('/var/crash/_usr_bin_update-manager.0.crash'):
        report = Report()
        report.setdefault('Tags', 'dist-upgrade')
        report['Tags'] += ' dist-upgrade'
        _apport_append_logfiles(report)
        report.add_to_existing('/var/crash/_usr_bin_update-manager.0.crash')
    return True

def apport_pkgfailure(pkg, errormsg):
    logging.debug("running apport_pkgfailure() %s: %s", pkg, errormsg)
    LOGDIR="/var/log/dist-upgrade/"
    s = "/usr/share/apport/package_hook"

    # we do not report followup errors from earlier failures
    # dpkg messages will not be translated if DPKG_UNTRANSLATED_MESSAGES is
    # set which it is by default so check for the English message first
    if "dependency problems - leaving unconfigured" in errormsg:
        return False
    if gettext.dgettext('dpkg', "dependency problems - leaving unconfigured") in errormsg:
        return False
    # we do not run apport_pkgfailure for full disk errors
    if os.strerror(errno.ENOSPC) in errormsg:
        logging.debug("dpkg error because of full disk, not reporting against %s " % pkg)
        return False

    if os.path.exists(s):
        args = [s, "-p", pkg]
        for fname in APPORT_WHITELIST:
            args.extend(["-l", os.path.join(LOGDIR, fname)])
        try:
            p = subprocess.Popen(args, stdin=subprocess.PIPE)
            p.stdin.write("ErrorMessage: %s\n" % errormsg)
            p.stdin.close()
            #p.wait()
        except Exception, e:
            logging.warning("Failed to run apport (%s)" % e)
            return False
        return True
    return False

def run_apport():
    " run apport, check if we have a display "
    if "RELEASE_UPRADER_NO_APPORT" in os.environ:
        logging.debug("RELEASE_UPRADER_NO_APPORT env set")
        return False
    if "DISPLAY" in os.environ:
        for p in ["/usr/share/apport/apport-gtk", "/usr/share/apport/apport-qt"]:
            if os.path.exists(p):
                ret = -1
                try:
                    ret = subprocess.call(p)
                except Exception:
                    logging.exception("Unable to launch '%s' " % p)
                return (ret == 0)
    elif os.path.exists("/usr/bin/apport-cli"):
        try:
            return (subprocess.call("/usr/bin/apport-cli") == 0)
        except Exception:
            logging.exception("Unable to launch '/usr/bin/apport-cli'")
            return False
    logging.debug("can't find apport")
    return False


if __name__ == "__main__":
    apport_crash(None, None, None)
