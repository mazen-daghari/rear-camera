from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEngineScript

def enable_adblock():
    profile = QWebEngineProfile.defaultProfile()
    adblock_script = QWebEngineScript()
    adblock_script.setName("AdBlock")
    adblock_script.setSourceCode("""
        (function() {
            var observer = new MutationObserver(function(mutations) {
                mutations.forEach(function(mutation) {
                    if (mutation.addedNodes.length) {
                        mutation.addedNodes.forEach(function(node) {
                            if (node.nodeType === 1) {
                                if (node.matches('iframe, .ad, .ads, [id^="ad-"], [class*="ad-"], [class*="ads-"], [class*="ad_"], [class*="ads_"], [id*="ad_"], [id*="ads_"]')) {
                                    node.remove();
                                }
                            }
                        });
                    }
                });
            });
            observer.observe(document.body, { childList: true, subtree: true });
        })();
    """)
    adblock_script.setInjectionPoint(QWebEngineScript.DocumentCreation)
    adblock_script.setWorldId(QWebEngineScript.MainWorld)
    adblock_script.setRunsOnSubFrames(True)
    profile.scripts().insert(adblock_script)
