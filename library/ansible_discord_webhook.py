#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: discord_webhook

short_description: Sending messages using Discord webhooks.

version_added: "2.7"

description:
    - "This is a simple module for sending messages using Discord webhooks using the python requests library."

author: Sam Wedgwood (@shadycake)

options:
    webhook_url:
        description:
            - The url of the webhook as given by the Discord app.
        required: true
        type: string
    content:
        description:
            - Content of the message to send using the webhook.
        type: string
        required: true
    username:
        description:
            - Override the default username of the webhook.
        type: string
    avatar_url:
        description:
            - Override the default avatar of the webhook using a url.
        type: string
    tts:
        description:
            - Set this to true if this is a Text-To-Speech (TTS) message.
        type: bool
        default: false

requirements:
    - requests>=2.20.0
'''

EXAMPLES = '''
# sending a message
- name: Send Hello World! to the webhook
  discord_webhook:
    webhook_url: https://canary.discordapp.com/api/webhooks/XXXXXXXXXXXXXXXXXX/XXXXXXXXXXXXXXXXXXXXX
    content: Hello, world!

# pass in a message and have changed true
- name: Send Hello World! to the webhook under CoolDude username
  discord_webhook:
    webhook_url: https://canary.discordapp.com/api/webhooks/XXXXXXXXXXXXXXXXXX/XXXXXXXXXXXXXXXXXXXXX
    content: Hello, world!
    username: CoolDude
'''

RETURN = '''
error:
    description: The error, if returned by the discord api.
    returned: on error
    type: complex
    sample: [50006, "Cannot send an empty message"]
    contains:
        - integer
        - string
'''

from ansible.module_utils.basic import AnsibleModule
import requests

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = {
        "webhook_url": {
            "type": "str",
            "required": True
        },
        "content": {
            "type": "str",
            "required": True,
        },
        "username": {
            "type": "str",
            "required": False
        },
        "avatar_url": {
            "type": "str",
            "required": False
        },
        "tts": {
            "type": "bool",
            "required": False,
            "default": False
        }
    }

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = {
        "changed": False
    }

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    url = module.params["webhook_url"]
    data = {
        "content": module.params["content"]
    }
    username = module.params.get("username")
    avatar_url = module.params.get("avatar_url")
    tts = module.params.get("tts")

    if username:
        data["username"] = username
    if avatar_url:
        data["avatar_url"] = avatar_url
    if tts:
        data["tts"] = module.params.get("tts")

    request = requests.post(url, json=data)

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
