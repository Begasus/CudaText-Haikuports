EVENTS = [
    'on_app_activate',
    'on_app_deactivate',
    'on_caret',
    'on_caret_slow',
    'on_change',
    'on_change_slow',
    'on_cli',
    'on_click',
    'on_click_dbl',
    'on_click_gap',
    'on_click_gutter',
    'on_click_link',
    'on_click_right',
    'on_close',
    'on_close_pre',
    'on_complete',
    'on_console_nav',
    'on_delete_file',
    'on_exit',
    'on_focus',
    'on_func_hint',
    'on_goto_def',
    'on_goto_enter',
    'on_hotspot',
    'on_insert',
    'on_key',
    'on_key_up',
    'on_lexer',
    'on_lexer_parsed',
    'on_macro',
    'on_message',
    'on_mouse_stop',
    'on_open',
    'on_open_none',
    'on_open_pre',
    'on_output_nav',
    'on_paste',
    'on_save',
    'on_save_pre',
    'on_save_naming',
    'on_scroll',
    'on_sidebar_popup',
    'on_snippet',
    'on_start',
    'on_start2',
    'on_state',
    'on_state_ed',
    'on_tab_change',
    'on_tab_menu',
    'on_tab_move',
  ]

EVENTS_ADD_PARAMS = {
  'on_key': 'key, state',
  'on_key_up': 'key, state',
  'on_insert': 'text',
  'on_cli': 'param1, param2',
  'on_click': 'state',
  'on_click_dbl': 'state',
  'on_click_right': 'state',
  'on_click_gap': 'state, nline, ntag, size_x, size_y, pos_x, pos_y',
  'on_click_gutter': 'state, nline, nband',
  'on_click_link': 'state, link',
  'on_console_nav': 'text',
  'on_delete_file': 'filename',
  'on_goto_enter': 'text',
  'on_hotspot': 'entered, hotspot_index',
  'on_output_nav': 'text, tag',
  'on_macro': 'text',
  'on_message': 'id, text',
  'on_mouse_stop': 'x, y',
  'on_open_pre': 'filename',
  'on_paste': 'keep_caret, select_then',
  'on_snippet': 'snippet_id, snippet_text',
  'on_state': 'state',
  'on_state_ed': 'state',
  'on_sidebar_popup': 'caption',
  }