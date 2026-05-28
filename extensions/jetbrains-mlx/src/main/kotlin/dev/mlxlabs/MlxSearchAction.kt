package dev.mlxlabs

import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.ui.popup.JBPopupFactory
import com.intellij.openapi.ui.popup.PopupStep
import com.intellij.openapi.ui.popup.util.BaseListPopupStep
import com.intellij.ide.BrowserUtil
import java.io.File

class MlxSearchAction : AnAction() {
    override fun actionPerformed(e: AnActionEvent) {
        val project = e.project ?: return
        val basePath = project.basePath ?: return
        val file = File(basePath, "docs/api/endpoints.json")
        if (!file.exists()) {
            BrowserUtil.browse("https://github.com/multilogin-labs/multilogin-labs")
            return
        }
        val text = file.readText()
        val rx = Regex("\"name\":\\s*\"([^\"]+)\"|\"slug\":\\s*\"([^\"]+)\"|\"method\":\\s*\"([^\"]+)\"")
        val items = mutableListOf<Triple<String, String, String>>()
        var name = ""
        var method = ""
        for (m in rx.findAll(text)) {
            when {
                m.groups[1] != null -> name = m.groups[1]!!.value
                m.groups[3] != null -> method = m.groups[3]!!.value
                m.groups[2] != null -> {
                    items += Triple(method, name, m.groups[2]!!.value)
                    name = ""
                    method = ""
                }
            }
        }
        val display = items.map { "${it.first.padEnd(6)} ${it.second}" }
        val popup = JBPopupFactory.getInstance().createListPopup(object : BaseListPopupStep<String>(
            "Multilogin X API · ${items.size} endpoints",
            display,
        ) {
            override fun onChosen(selectedValue: String, finalChoice: Boolean): PopupStep<*>? {
                val idx = display.indexOf(selectedValue)
                if (idx >= 0) {
                    val slug = items[idx].third
                    BrowserUtil.browse(
                        "https://github.com/multilogin-labs/multilogin-labs/blob/main/docs/api/endpoints/$slug.md",
                    )
                }
                return null
            }
        })
        popup.showInBestPositionFor(e.dataContext)
    }
}
