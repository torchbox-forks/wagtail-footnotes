// wagtail_footnotes/static/footnotes/js/read-only-uuid-controller.js

class CustomEditorController extends window.StimulusModule.Controller {
    connect() {
        setUUID(this.element.id);
    }
}

window.wagtail.app.register('read-only-uuid', CustomEditorController);
