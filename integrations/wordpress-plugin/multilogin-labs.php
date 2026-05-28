<?php
/**
 * Plugin Name:       Multilogin Labs
 * Plugin URI:        https://github.com/multilogin-labs/multilogin-labs
 * Description:       Adds a [mlx_partner] shortcode that renders the official Multilogin partner CTA with promo codes.
 * Version:           0.1.0
 * Author:            Multilogin Labs
 * Author URI:        https://github.com/multilogin-labs
 * License:           MIT
 * Text Domain:       multilogin-labs
 *
 * Usage in any post or page:
 *   [mlx_partner]
 *   [mlx_partner label="Try Multilogin" theme="dark"]
 */

if ( ! defined( 'ABSPATH' ) ) exit;

const MLX_PARTNER_URL = 'https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549';

function mlx_partner_shortcode( $atts ) {
    $atts = shortcode_atts(
        array(
            'label' => 'Start $2 trial · SAAS50',
            'theme' => 'light',
        ),
        $atts,
        'mlx_partner'
    );

    $bg = $atts['theme'] === 'dark' ? '#0d1117' : '#f6f8fa';
    $fg = $atts['theme'] === 'dark' ? '#e6edf3' : '#0d1117';
    $accent = '#0066FF';

    $url = esc_url( MLX_PARTNER_URL );
    $label = esc_html( $atts['label'] );

    return sprintf(
        '<div style="display:inline-block;padding:1rem 1.25rem;border-radius:8px;background:%s;color:%s;font-family:system-ui,sans-serif;border:1px solid %s33;max-width:540px"><div style="font-weight:700;color:%s;margin-bottom:.25rem">Multilogin · official partner</div><div style="font-size:.9rem;margin-bottom:.5rem">90 API endpoints · cloud phone · antidetect</div><a href="%s" rel="noopener" target="_blank" style="display:inline-block;padding:.55rem 1rem;background:%s;color:#fff;border-radius:6px;text-decoration:none;font-weight:600">%s</a> <span style="font-size:.8rem;opacity:.7">codes <strong>SAAS50</strong> · <strong>MIN50</strong></span></div>',
        $bg,
        $fg,
        $accent,
        $accent,
        $url,
        $accent,
        $label
    );
}
add_shortcode( 'mlx_partner', 'mlx_partner_shortcode' );

function mlx_partner_settings_link( $links ) {
    $links[] = '<a href="' . MLX_PARTNER_URL . '" target="_blank" rel="noopener">Partner pricing</a>';
    return $links;
}
add_filter( 'plugin_row_meta', 'mlx_partner_settings_link', 10, 2 );
