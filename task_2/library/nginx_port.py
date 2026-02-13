#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            port=dict(type='int', required=True)
        ),
        supports_check_mode=True
    )

    port = module.params['port']

    try:
        config = f"""
server {{
    listen {port};
    server_name _;
    location /files {{
        autoindex on;
        alias /var/www/files/;
    }}
}}
"""
        with open("/etc/nginx/sites-available/files", "w") as f:
            f.write(config)

        module.exit_json(changed=True, msg=f"Nginx port set to {port}")

    except Exception as e:
        module.fail_json(msg=str(e))

if __name__ == "__main__":
    main()