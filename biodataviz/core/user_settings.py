import ipywidgets as w

from abc import ABC, abstractmethod


class UserSettings(ABC):

    def __init__(self) -> None:
        vbox_with_user_settings_widgets = self._build_vbox_with_user_settings_widgets()
        self.configurable_widgets = self._get_all_configurable_widgets()
        self.widget = self._build_widget(vbox_with_user_settings_widgets)

    
    @property
    @abstractmethod
    def accordion_title(self) -> str:
        accordion_title = 'Specify the accordion title that describes the configurable components here'
        return accordion_title

    @abstractmethod
    def _build_vbox_with_user_settings_widgets(self) -> w.VBox:
        # Combine all user_settings widgets here into a single VBox
        # Make sure to create all user_settings_widgets as attribute! Like so:
        # self.user_settings_widget = w.Text(description = 'Just an:', value = 'example')
        pass


    def export_current_settings(self) -> dict[str, float | int | str | bool]:
        configs = {attribute_name.removeprefix('user_settings_'): widget.value for attribute_name, widget in self.configurable_widgets.items()}
        return configs


    def _get_all_configurable_widgets(self) -> dict[str, w.Widget]:
        all_instance_attributes = vars(self)
        all_class_attributes = vars(self.__class__)
        all_attributes = {**all_instance_attributes, **all_class_attributes}
        all_configurable_widgets = {name: attribute for name, attribute in all_attributes.items() if name.startswith('user_settings_')}
        return all_configurable_widgets

    
    def _build_widget(self, vbox_with_user_settings_widgets: w.VBox) -> w.Accordion:
        accordion = w.Accordion(children = [vbox_with_user_settings_widgets],
                                titles = (self.accordion_title, ),
                                selected_index = None)
        return accordion



class UserSettingsView(ABC):

    @property
    @abstractmethod
    def _all_user_settings_to_create(self) -> list[UserSettings]:  
        # Create a list here of all specific UserSettings classes
        pass

    def __init__(self) -> None:
        self._instantiate_all_user_settings()
        self.widget = self._build_widget()


    def _instantiate_all_user_settings(self) -> None:
        if hasattr(self, 'all_user_settings') == False:
            all_user_settings = [user_settings() for user_settings in self._all_user_settings_to_create]
            setattr(self, 'all_user_settings', all_user_settings)


    def export_all_user_settings(self) -> dict:
        all_user_settings = {}
        for user_settings in self.all_user_settings:
            individual_user_settings = user_settings.export_current_settings()
            all_user_settings = {**all_user_settings, **individual_user_settings}
        return all_user_settings


    def _build_widget(self) -> w.VBox:
        vbox_all_individual_config_accordions = w.VBox([user_settings.widget for user_settings in self.all_user_settings])
        self.refresh_plot_button = w.Button(description = 'Refresh the plot')
        self.save_plot_button = w.Button(description = 'Save the plot')
        full_configs_box = w.VBox([vbox_all_individual_config_accordions,
                                   w.HBox([self.refresh_plot_button, self.save_plot_button])])
        self.plot_output = w.Output()
        self.gallery_accordion = w.Accordion(children = [w.Text()], 
                                             titles = ('Want to change the plot? Checkout our gallery of all available plots!', ),
                                             selected_index = None)
        full_widget = w.VBox([w.HBox([full_configs_box, self.plot_output]),
                              self.gallery_accordion])
        return full_widget






        